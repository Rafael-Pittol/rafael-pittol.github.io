# Instruções para Agentes de IA - Projetos Python

## Visão Geral
Este repositório é uma coleção de projetos pessoais de aprendizagem em **Python** (backend/desktop) e **web** (HTML/CSS/JavaScript). Cada pasta é um projeto independente com diferentes tecnologias e padrões.

## Estrutura de Projetos

### Projetos Python
- **Calculadora/** - Aplicativo desktop com interface gráfica usando [Flet](https://flet.dev/)
- **Snake jogo/** - Jogo 2D usando [Pygame](https://www.pygame.org/)

### Projetos Web
- **iphone/** - Demonstração interativa do iPhone 14 com Dynamic Islands (HTML/CSS)
- **Matrix/** - Visualização animada de Matrix em Canvas (HTML/JavaScript)
- **Meu Site/** - Portfólio pessoal (HTML/CSS)
- **Propaganda/** - Página de marketing (HTML/CSS)

## Padrões de Desenvolvimento

### Python - Flet (Calculadora)
- **Padrão**: Aplicação desktop com componentes reativos
- **Handler Pattern**: Funções `on_click` com `nonlocal` para estado compartilhado
- **Estilos**: Dicionários de estilos reutilizáveis (`estilo_numeros`, `estilo_operadores`)
- **Layout**: `Column` para grupos verticais, `Row` para grupos horizontais
- **Exemplo prático**:
  - Use `nonlocal` para modificar variáveis do escopo externo
  - Separar lógica (handlers) da apresentação (componentes Flet)
  - Agrupar estilos em dicts para reutilização

### Python - Pygame (Snake)
- **Padrão**: Game loop com event handling
- **Estrutura**: Inicialização global → Loop infinito com eventos/física/render
- **Variáveis Globais**: `head_pos`, `snake_body`, `food_pos`, `direction` (inicializado em `init_vars()`)
- **Exemplo prático**:
  - Manter largura/altura do frame como constantes (`frame_size_x`, `frame_size_y`)
  - Usar `pygame.Color` para consistência de cores
  - Separar lógica de score em funções auxiliares

### Web - HTML/CSS
- **HTML Semântico**: Usar tags de estrutura (`nav`, `header`, `main`, `section`)
- **CSS Modular**: Arquivo separado (`style.css`) para cada projeto web
- **Temas Dinâmicos**: Usar `input[type="radio"]` + CSS seletores (ex: `#deep-purple:checked`)
- **Canvas 2D**: Usar `canvas.getContext("2d")` e re-renderizar em animation frames
- **Responsividade**: `viewport` meta tag e event listeners para resize

### Web - JavaScript
- **Padrão Canvas**: Requisição do contexto 2D, dimensões dinâmicas
- **Event Listeners**: `resize`, `keydown`, `QUIT` para controles
- **Arrays de Caracteres**: Usar arrays para variações visuais (chars, cores)
- **Exemplo prático**:
  - Atualizar canvas ao fazer resize da janela
  - Usar `console.log` para debugging

## Fluxos de Trabalho Críticos

### Executar Aplicação Flet
```bash
cd Calculadora
python -m flet Calculadora.py
```

### Executar Jogo Pygame
```bash
cd "Snake jogo"
python snake.py
```

### Visualizar Projetos Web
Abrir arquivos `.html` diretamente no navegador ou usar live server.

## Convenções do Projeto

- **Nomes em Português**: Variáveis, funções e comentários frequentemente em português
- **Sem Package Manager**: Projetos usam dependências nativas (`flet`, `pygame`)
- **Sem Tests Automatizados**: Usar validação manual estruturada
- **Desktop Window Config**: Dimensões fixas em aplicações desktop (ex: `page.window.width = 350`)

## Tests

- Este repositório não possui testes automatizados por padrão.
- Ao alterar código, executar validação manual do fluxo principal.
- Se ocorrer erro ou comportamento inesperado, registrar mensagem, stack trace e passos de reprodução, e sugerir uma correção inicial.

## Tratamento de Erros

### Validação Manual e Debugging
- Se um erro ocorrer durante validação manual, registre detalhes do erro (stack trace, condições de reprodução)
- Sugira uma possível correção baseada no contexto do projeto e padrões estabelecidos
- Para aplicações Flet: verificar estado compartilhado com `nonlocal` e listeners de eventos
- Para Pygame: validar inicialização de variáveis globais e detecção de colisões
- Para Web: usar `console.log` e ferramentas de dev do navegador para rastreamento

### Erros Comuns
- **ImportError**: Verificar instalação de dependências (`pip install flet pygame`). Se uma dependência necessária estiver faltando, solicite ao usuário que a instale usando pip antes de executar o projeto
- **Dimensão inválida**: Validar `frame_size_x`, `frame_size_y` e dimensões do canvas
- **Referência indefinida**: Confirmar que variáveis globais foram inicializadas em `init_vars()`

### Validação de Dependências
Sempre que trabalhar com projetos Python, verifique se as dependências externas estão instaladas:
- Para **Calculadora (Flet)**: Execute `pip install flet` antes de rodar a aplicação
- Para **Snake jogo (Pygame)**: Execute `pip install pygame` antes de rodar o jogo
- Se o usuário encontrar erro de importação, solicitar a instalação da dependência correspondente.

## Dependências Externas

| Projeto | Dependência | Propósito |
|---------|------------|----------|
| Calculadora | `flet` | Framework UI desktop multiplataforma |
| Snake jogo | `pygame` | Motor de jogo 2D |
| Todos Web | Nenhuma | HTML/CSS/JS puro |

**Nota**: Se faltar dependência, instalar com pip conforme o projeto.

## Resolução de Conflitos de Prioridades

Quando **simplicidade** e **responsividade** entrarem em conflito, a decisão deve seguir o objetivo principal de cada tipo de projeto:

- **Projetos Python (desktop)**: Priorizar **simplicidade** e funcionalidade direta. Código simples e direto é preferível à otimização visual.
- **Projetos Web**: Priorizar **responsividade** e experiência do usuário fluida. Layout adaptativo e performance visual são críticos.

**Regra de Resolução (obrigatória)**: Em qualquer trade-off, aplicar esta ordem:
1. Garantir funcionamento correto.
2. Aplicar a prioridade do tipo de projeto (desktop: simplicidade; web: responsividade).
3. Persistindo empate, escolher a alternativa mais simples de manter.

## Referências de Código

- **Componentes Flet**: `ft.ElevatedButton`, `ft.Column`, `ft.Row`, `ft.Container`, `ft.Text`
- **Pygame**: `pygame.display`, `pygame.event`, `pygame.time.Clock`, `pygame.font`
- **Canvas JS**: `canvas.getContext("2d")`, `fillRect()`, `drawImage()`

## Dicas para Agentes IA

1. Cada projeto é independente - não há dependências cruzadas
2. Projetos Python usam `nonlocal` para estado compartilhado; web usa objetos/closures
3. Verificar dimensões de tela/canvas ao trabalhar com layout/renderização
4. **Convenção de Nomenclatura**: Regra determinística:
  - Se o arquivo tiver padrão claro, manter o padrão existente.
  - Se o padrão estiver inconsistente ou indefinido, usar português para nomes de variáveis, funções e comentários novos.
  - Se o arquivo misturar português e inglês, padronizar novas adições para português.
  - Exceção: nomes de bibliotecas externas, tipos built-in e keywords Python permanecem em inglês.
5. **Priorização de Conflitos**: Usar apenas a regra da seção "Resolução de Conflitos de Prioridades".
