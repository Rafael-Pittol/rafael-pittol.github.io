import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora"
    page.bgcolor = "#0b1020"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 350
    page.window.height = 560
    page.window.resizable = False

    todos_valores = ""
    operadores = {"%", "/", "*", "-", "+"}
    operador_ativo = None
    botoes_operadores = {}
    botao_igual = None

    resultado_texto = ft.Text(
        value="0",
        size=42,
        color="#e8edf7",
        text_align=ft.TextAlign.RIGHT,
        weight=ft.FontWeight.W_500,
    )

    def criar_estilo_botao(estilo):
        return ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            padding=0,
            animation_duration=220,
            bgcolor={
                ft.ControlState.DEFAULT: estilo["bgcolor"],
                ft.ControlState.HOVERED: estilo["hover_color"],
                ft.ControlState.PRESSED: estilo["pressed_color"],
            },
            elevation={
                ft.ControlState.DEFAULT: 2,
                ft.ControlState.HOVERED: 6,
                ft.ControlState.PRESSED: 1,
            },
        )

    def atualizar_destaque_operador():
        for op, botao in botoes_operadores.items():
            if op == operador_ativo:
                botao.style = criar_estilo_botao(estilo_operador_ativo)
            else:
                botao.style = criar_estilo_botao(estilo_operadores)

    def expressao_pronta_para_calculo():
        if not todos_valores:
            return False
        if todos_valores[-1] in operadores or todos_valores[-1] == ".":
            return False
        try:
            eval(todos_valores)
            return True
        except:
            return False

    def atualizar_destaque_igual():
        if botao_igual is None:
            return
        if expressao_pronta_para_calculo():
            botao_igual.style = criar_estilo_botao(estilo_equal_ativo)
        else:
            botao_igual.style = criar_estilo_botao(estilo_equal)

    def atualizar_operador_ativo_por_expressao():
        nonlocal operador_ativo
        if todos_valores and todos_valores[-1] in operadores:
            operador_ativo = todos_valores[-1]
        else:
            operador_ativo = None
        atualizar_destaque_operador()
        atualizar_destaque_igual()

    def entrar_valores (e):
        nonlocal todos_valores, operador_ativo
        valor = str(e.control.content.value)
        todos_valores += valor
        resultado_texto.value = todos_valores

        if valor in operadores:
            operador_ativo = valor
        else:
            operador_ativo = None
        atualizar_destaque_operador()
        atualizar_destaque_igual()
        page.update()

    def limpar_tela(e):
        nonlocal todos_valores, operador_ativo
        todos_valores = ""
        operador_ativo = None
        atualizar_destaque_operador()
        atualizar_destaque_igual()
        resultado_texto.value = "0"
        page.update()

    def calcular(e):
        nonlocal todos_valores, operador_ativo
        try:
            resultado_texto.value = str(eval(todos_valores))
            todos_valores = resultado_texto.value
            operador_ativo = None
            atualizar_destaque_operador()
            atualizar_destaque_igual()
        except:
            resultado_texto.value = "Erro"
            todos_valores = ""
            operador_ativo = None
            atualizar_destaque_operador()
            atualizar_destaque_igual()
        page.update()

    def apagar_ultimo(e):
        nonlocal todos_valores
        todos_valores = todos_valores[:-1]
        atualizar_operador_ativo_por_expressao()
        resultado_texto.value = todos_valores if todos_valores else "0"
        page.update()        

    tela = ft.Container(
        content=resultado_texto,
        bgcolor="#111729",
        padding=ft.Padding.only(left=16, right=16, top=18, bottom=18),
        border_radius=14,
        height=95,
        alignment=ft.alignment.Alignment(1, 0),
        border=ft.Border.all(1, "#2a3550"),
    )

    # estilizacao dos botoes
    estilo_numeros = {
        "height":64,
        "bgcolor":"#27324a",
        "hover_color":"#33405d",
        "pressed_color":"#1d273b",
        "color":"#f5f8ff",
        "expand":1,
    }

    estilo_operadores = {
        "height":64,
        "bgcolor":"#3c63ff",
        "hover_color":"#4f73ff",
        "pressed_color":"#2f50db",
        "color":"#ffffff",
        "expand":1,
    }

    estilo_operador_ativo = {
        "height":64,
        "bgcolor":"#00b7ff",
        "hover_color":"#29c5ff",
        "pressed_color":"#009ad8",
        "color":"#ffffff",
        "expand":1,
    }

    estilo_limpar = {
        "height":64,
        "bgcolor":"#f05b6d",
        "hover_color":"#f46f7e",
        "pressed_color":"#d94a5b",
        "color":"#ffffff",
        "expand":1,
    }

    estilo_equal = {
        "height":64,
        "bgcolor":"#ff8a3d",
        "hover_color":"#ff9a56",
        "pressed_color":"#e46f2d",
        "color":"#ffffff",
        "expand":1,
    }

    estilo_equal_ativo = {
        "height":64,
        "bgcolor":"#28c76f",
        "hover_color":"#3ad781",
        "pressed_color":"#1eab5d",
        "color":"#ffffff",
        "expand":1,
    }

    grelha_de_botoes = [
        
        [
            ("C",estilo_limpar,limpar_tela),
            ("%",estilo_operadores,entrar_valores),
            ("/",estilo_operadores,entrar_valores),
            ("*",estilo_operadores,entrar_valores)
        ],

         [
            ("7",estilo_numeros,entrar_valores),
            ("8",estilo_numeros,entrar_valores),
            ("9",estilo_numeros,entrar_valores),
            ("-",estilo_operadores,entrar_valores)
        ],

         [
            ("4",estilo_numeros,entrar_valores),
            ("5",estilo_numeros,entrar_valores),
            ("6",estilo_numeros,entrar_valores),
            ("+",estilo_operadores,entrar_valores)
        ],

         [
            ("1",estilo_numeros,entrar_valores),
            ("2",estilo_numeros,entrar_valores),
            ("3",estilo_numeros,entrar_valores),
            ("=",estilo_equal,calcular)
        ],

         [
            ("0",{**estilo_numeros, "expand":2},entrar_valores),
            (".",estilo_numeros,entrar_valores),
            ("⌫",estilo_operadores, apagar_ultimo)
        ],

    ]

    botoes = []

    for linha in grelha_de_botoes:
        linha_control = []
        for texto, estilo, handler in linha:
            btn = ft.Button(
                content=ft.Text(texto, size=20, weight=ft.FontWeight.W_600),
                on_click=handler,
                height=estilo["height"],
                bgcolor=estilo["bgcolor"],
                color=estilo["color"],
                expand=estilo["expand"],
                style=criar_estilo_botao(estilo)

            )
            if texto in operadores:
                botoes_operadores[texto] = btn
            if texto == "=":
                botao_igual = btn
            linha_control.append(btn)
        botoes.append(ft.Row(linha_control, spacing=8))

    cartao = ft.Container(
        width=320,
        padding=18,
        border_radius=22,
        opacity=0,
        scale=0.97,
        animate_opacity=ft.Animation(350, ft.AnimationCurve.EASE_OUT),
        animate_scale=ft.Animation(420, ft.AnimationCurve.EASE_OUT_CUBIC),
        gradient=ft.LinearGradient(
            begin=ft.alignment.Alignment(-1, -1),
            end=ft.alignment.Alignment(1, 1),
            colors=["#141c31", "#0f1526"],
        ),
        border=ft.Border.all(1, "#2a3656"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=24,
            color="#70000000",
            offset=ft.Offset(0, 10),
        ),
        content=ft.Column(
            [
                ft.Text(
                    "Calculadora",
                    size=16,
                    color="#94a3c8",
                    weight=ft.FontWeight.W_500,
                ),
                tela,
                ft.Column(botoes, spacing=8),
            ],
            spacing=12,
        ),
    )

    page.add(cartao)
    atualizar_destaque_igual()
    cartao.opacity = 1
    cartao.scale = 1
    page.update()

ft.run(main)   