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
python -m flet Calculadora/Calculadora.py
```

### Executar Jogo Pygame
```bash
python Snake\ jogo/snake.py
```

### Visualizar Projetos Web
Abrir arquivos `.html` diretamente no navegador ou usar live server.

## Convenções do Projeto

- **Nomes em Português**: Variáveis, funções e comentários frequentemente em português
- **Sem Package Manager**: Projetos usam dependências nativas (`flet`, `pygame`)
- **Sem Tests Automatizados**: Validação manual/iterativa. If an error occurs during manual validation, log the error details and suggest a possible fix.
- **Desktop Window Config**: Dimensões fixas em aplicações desktop (ex: `page.window.width = 350`)

## Dependências Externas

| Projeto | Dependência | Propósito |
|---------|------------|----------|
| Calculadora | `flet` | Framework UI desktop multiplataforma |
| Snake jogo | `pygame` | Motor de jogo 2D |
| Todos Web | Nenhuma | HTML/CSS/JS puro |

## Referências de Código

- **Componentes Flet**: `ft.ElevatedButton`, `ft.Column`, `ft.Row`, `ft.Container`, `ft.Text`
- **Pygame**: `pygame.display`, `pygame.event`, `pygame.time.Clock`, `pygame.font`
- **Canvas JS**: `canvas.getContext("2d")`, `fillRect()`, `drawImage()`

## Dicas para Agentes IA

1. Cada projeto é independente - não há dependências cruzadas
2. Projetos Python usam `nonlocal` para estado compartilhado; web usa objetos/closures
3. Verificar dimensões de tela/canvas ao trabalhar com layout/renderização
4. If the local file standard is unclear, default to using Portuguese for all variable names and comments.
5. When simplicity and responsiveness conflict, prioritize the primary goal of the project type.
