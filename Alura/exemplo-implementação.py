class BaseDeConhecimento:
    def __init__(self):
        self.fatos = []
        self.regras = []

    def adicionar_fato(self, fato):
        self.fatos.append(fato)

    def adicionar_regra(self, condicao, conclusao):
        self.regras.append((condicao, conclusao))

    def carregar_fatos(self, fatos):
        for fato in fatos:
            if fato not in self.fatos:
                self.fatos.append(fato)

    def carregar_regras_logicas(self, regras_logicas):
        for regra in regras_logicas:
            condicao, conclusao = parsear_regra_logica(regra)
            self.adicionar_regra(condicao, conclusao)


def parsear_regra_logica(regra):
    texto = regra.strip()

    # Aceita tanto "->" quanto "→" como operador de implicacao.
    if "->" in texto:
        partes = texto.split("->", 1)
    elif "→" in texto:
        partes = texto.split("→", 1)
    else:
        raise ValueError(f"Regra invalida (faltou implicacao): {regra}")

    esquerda = partes[0].strip().strip("()")
    direita = partes[1].strip().strip("()")

    if not esquerda or not direita:
        raise ValueError(f"Regra invalida (lado vazio): {regra}")

    # Aceita conectivos "∧" e "and" entre premissas.
    if "∧" in esquerda:
        condicao = [item.strip() for item in esquerda.split("∧") if item.strip()]
    else:
        condicao = [item.strip() for item in esquerda.split("and") if item.strip()]

    if not condicao:
        raise ValueError(f"Regra invalida (sem premissas): {regra}")

    return condicao, direita

class SistemaEspecialista:
    def __init__(self, base_conhecimento):
        self.base_conhecimento = base_conhecimento

    def _literal_satisfeito(self, literal):
        texto = literal.strip()

        # Suporte a negacao simples: "nao X", "não X", "not X" e "!X".
        if texto.startswith("nao "):
            return texto[4:].strip() not in self.base_conhecimento.fatos
        if texto.startswith("não "):
            return texto[4:].strip() not in self.base_conhecimento.fatos
        if texto.startswith("not "):
            return texto[4:].strip() not in self.base_conhecimento.fatos
        if texto.startswith("!"):
            return texto[1:].strip() not in self.base_conhecimento.fatos

        return texto in self.base_conhecimento.fatos

    def _regra_aplicavel(self, condicoes):
        return all(self._literal_satisfeito(condicao) for condicao in condicoes)

    def inferir(self):
        houve_mudanca = True
        while houve_mudanca:
            houve_mudanca = False
            for condicao, conclusao in self.base_conhecimento.regras:
                if self._regra_aplicavel(condicao) and conclusao not in self.base_conhecimento.fatos:
                    self.base_conhecimento.fatos.append(conclusao)
                    houve_mudanca = True

        return self.base_conhecimento.fatos

    def diagnosticar(self, diagnosticos_possiveis):
        fatos_finais = self.inferir()
        for diagnostico in diagnosticos_possiveis:
            if diagnostico in fatos_finais:
                return diagnostico
        return "inconclusivo"

# Regras logicas no formato: (P ∧ Q) -> R
regras_logicas = [
    "(febre alta ∧ tosse) -> infecção respiratória",
    "(infecção respiratória ∧ dificuldade para respirar) -> pneumonia",
    "(febre and tosse and dor no corpo) -> suspeita gripe",
    "(suspeita gripe and coriza) -> diagnóstico gripe",
    "(febre and tosse seca and perda de olfato) -> suspeita covid",
    "(suspeita covid and falta de ar) -> diagnóstico covid",
    "(dor abdominal and náusea and not febre) -> diagnóstico gastrite",
]

diagnosticos_prioridade = [
    "pneumonia",
    "diagnóstico covid",
    "diagnóstico gripe",
    "diagnóstico gastrite",
]

casos_pacientes = [
    {
        "paciente": "Paciente A",
        "sintomas": ["febre", "tosse", "dor no corpo", "coriza"],
        "esperado": "diagnóstico gripe",
    },
    {
        "paciente": "Paciente B",
        "sintomas": ["febre", "tosse seca", "perda de olfato", "falta de ar"],
        "esperado": "diagnóstico covid",
    },
    {
        "paciente": "Paciente C",
        "sintomas": ["dor abdominal", "náusea"],
        "esperado": "diagnóstico gastrite",
    },
    {
        "paciente": "Paciente D",
        "sintomas": ["febre alta", "tosse", "dificuldade para respirar"],
        "esperado": "pneumonia",
    },
]

acertos = 0

for caso in casos_pacientes:
    base = BaseDeConhecimento()
    base.carregar_fatos(caso["sintomas"])
    base.carregar_regras_logicas(regras_logicas)

    sistema = SistemaEspecialista(base)
    diagnostico = sistema.diagnosticar(diagnosticos_prioridade)

    acertou = diagnostico == caso["esperado"]
    if acertou:
        acertos += 1

    print(f"\n=== {caso['paciente']} ===")
    print("Sintomas relatados:", ", ".join(caso["sintomas"]))
    print("Diagnóstico esperado:", caso["esperado"])
    print("Diagnóstico inferido:", diagnostico)
    print("Status:", "OK" if acertou else "ERRO")

print(f"\nResumo: {acertos}/{len(casos_pacientes)} diagnósticos corretos.")