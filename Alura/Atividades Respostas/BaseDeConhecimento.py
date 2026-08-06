class BaseDeConhecimento:
	def __init__(self):
		self.fatos = []
		self.regras = []

	def adicionar_fato(self, fato):
		self.fatos.append(fato)

	def adicionar_regra(self, condicoes, conclusao):
		self.regras.append((condicoes, conclusao))


class SistemaEspecialista:
	def __init__(self, base_de_conhecimento):
		self.base_de_conhecimento = base_de_conhecimento
		self.fatos_inferidos = set(base_de_conhecimento.fatos)
		self.justificativas = {}

	def _literal_satisfeito(self, literal):
		if literal.startswith("nao "):
			fato_negado = literal[4:]
			return fato_negado not in self.fatos_inferidos

		if literal.startswith("não "):
			fato_negado = literal[4:]
			return fato_negado not in self.fatos_inferidos

		if literal.startswith("!"):
			fato_negado = literal[1:]
			return fato_negado not in self.fatos_inferidos

		return literal in self.fatos_inferidos

	def _regra_aplicavel(self, condicoes):
		return all(self._literal_satisfeito(condicao) for condicao in condicoes)

	def inferir(self):
		# Encadeamento progressivo: aplica regras ate nao gerar novos fatos.
		mudou = True
		while mudou:
			mudou = False
			for condicoes, conclusao in self.base_de_conhecimento.regras:
				if self._regra_aplicavel(condicoes) and conclusao not in self.fatos_inferidos:
					self.fatos_inferidos.add(conclusao)
					self.justificativas[conclusao] = list(condicoes)
					mudou = True

		return sorted(self.fatos_inferidos)

	def diagnosticar(self, diagnosticos_possiveis=None):
		fatos_finais = self.inferir()

		if diagnosticos_possiveis is None:
			return fatos_finais

		for diagnostico in diagnosticos_possiveis:
			if diagnostico in self.fatos_inferidos:
				return diagnostico

		return None

	def explicar(self, fato, nivel=0):
		indentacao = "  " * nivel

		if fato in self.base_de_conhecimento.fatos:
			return f"{indentacao}- '{fato}' foi informado como fato inicial."

		if fato not in self.justificativas:
			return f"{indentacao}- Nao ha justificativa registrada para '{fato}'."

		condicoes = self.justificativas[fato]
		linhas = [f"{indentacao}- '{fato}' foi inferido porque todas as condicoes abaixo foram satisfeitas:"]

		for condicao in condicoes:
			linhas.append(f"{indentacao}  * {condicao}")
			if condicao.startswith("nao ") or condicao.startswith("não ") or condicao.startswith("!"):
				linhas.append(f"{indentacao}    - condicao negativa verificada nos fatos atuais.")
			else:
				linhas.append(self.explicar(condicao, nivel + 2))

		return "\n".join(linhas)


if __name__ == "__main__":
	# Regras simplificadas para exemplo didatico de triagem medica.
	banco_regras = [
		(["febre", "tosse", "dor no corpo"], "suspeita gripe"),
		(["suspeita gripe", "coriza"], "diagnóstico gripe"),
		(["febre", "tosse seca", "perda de olfato"], "suspeita covid"),
		(["suspeita covid", "falta de ar"], "diagnóstico covid"),
		(["febre alta", "tosse"], "infecção respiratória"),
		(["infecção respiratória", "dificuldade para respirar"], "pneumonia"),
		(["dor abdominal", "náusea", "não febre"], "diagnóstico gastrite"),
	]

	casos = [
		{
			"paciente": "Paciente A",
			"fatos": ["febre", "tosse", "dor no corpo", "coriza"],
		},
		{
			"paciente": "Paciente B",
			"fatos": ["febre", "tosse seca", "perda de olfato", "falta de ar"],
		},
		{
			"paciente": "Paciente C",
			"fatos": ["dor abdominal", "náusea"],
		},
		{
			"paciente": "Paciente D",
			"fatos": ["febre alta", "tosse", "dificuldade para respirar"],
		},
	]

	diagnosticos_alvo = ["pneumonia", "diagnóstico covid", "diagnóstico gripe", "diagnóstico gastrite"]

	for caso in casos:
		base = BaseDeConhecimento()
		for fato in caso["fatos"]:
			base.adicionar_fato(fato)
		for condicoes, conclusao in banco_regras:
			base.adicionar_regra(condicoes, conclusao)

		sistema = SistemaEspecialista(base)
		diagnostico = sistema.diagnosticar(diagnosticos_alvo)

		print(f"\n=== {caso['paciente']} ===")
		print("Sintomas relatados:", ", ".join(caso["fatos"]))

		if diagnostico:
			print("Diagnostico deduzido:", diagnostico)
			print("Raciocinio seguido:")
			print(sistema.explicar(diagnostico))
		else:
			print("Diagnostico deduzido: inconclusivo")
			print("Raciocinio seguido: nenhuma regra de diagnostico foi totalmente satisfeita.")
