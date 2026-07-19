import flet as ft


def main(page: ft.Page):
    page.title = "Calculator"
    page.window.width = 400
    page.window.height = 650
    page.window.resizable = False
    page.bgcolor = "#000000"
    page.padding = ft.Padding.all(0)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # ---- State ----
    state = {
        "current": "0",     # value currently being typed / shown
        "operand": None,    # first operand stored
        "operator": None,   # pending operator
        "reset_next": False # whether next digit press should clear display
    }

    result_text = ft.Text(
        value="0",
        size=48,
        color="white",
        weight=ft.FontWeight.W_400,
        text_align=ft.TextAlign.RIGHT,
        max_lines=1,
    )

    expression_text = ft.Text(
        value="",
        size=18,
        color="#9e9e9e",
        text_align=ft.TextAlign.RIGHT,
        max_lines=1,
    )

    def update_display():
        result_text.value = state["current"]
        if state["operator"] and state["operand"] is not None:
            expression_text.value = f'{format_num(state["operand"])} {state["operator"]}'
        else:
            expression_text.value = ""
        page.update()

    def format_num(n):
        if isinstance(n, float) and n.is_integer():
            return str(int(n))
        return str(n)

    def calculate(a, b, op):
        try:
            if op == "+":
                return a + b
            elif op == "-":
                return a - b
            elif op == "×":
                return a * b
            elif op == "÷":
                if b == 0:
                    return "Error"
                return a / b
        except Exception:
            return "Error"

    def on_digit(e):
        digit = e.control.data
        if state["current"] == "0" or state["reset_next"]:
            state["current"] = digit
            state["reset_next"] = False
        else:
            if len(state["current"]) < 12:
                state["current"] += digit
        update_display()

    def on_decimal(e):
        if state["reset_next"]:
            state["current"] = "0"
            state["reset_next"] = False
        if "." not in state["current"]:
            state["current"] += "."
        update_display()

    def on_operator(e):
        op = e.control.data
        if state["operator"] and not state["reset_next"]:
            # chain operations
            a = state["operand"]
            b = float(state["current"])
            res = calculate(a, b, state["operator"])
            if res == "Error":
                state["current"] = "Error"
                state["operand"] = None
                state["operator"] = None
                state["reset_next"] = True
                update_display()
                return
            state["operand"] = res
            state["current"] = format_num(res)
        else:
            state["operand"] = float(state["current"])

        state["operator"] = op
        state["reset_next"] = True
        update_display()

    def on_equals(e):
        if state["operator"] is None:
            return
        a = state["operand"]
        b = float(state["current"])
        res = calculate(a, b, state["operator"])
        if res == "Error":
            state["current"] = "Error"
        else:
            state["current"] = format_num(round(res, 10))
        state["operand"] = None
        state["operator"] = None
        state["reset_next"] = True
        update_display()

    def on_clear(e):
        state["current"] = "0"
        state["operand"] = None
        state["operator"] = None
        state["reset_next"] = False
        update_display()

    def on_toggle_sign(e):
        try:
            val = float(state["current"])
            val = -val
            state["current"] = format_num(val)
        except ValueError:
            pass
        update_display()

    def on_percent(e):
        try:
            val = float(state["current"])
            val = val / 100
            state["current"] = format_num(val)
        except ValueError:
            pass
        update_display()

    def on_backspace(e):
        if state["reset_next"]:
            return
        cur = state["current"]
        if len(cur) <= 1 or (len(cur) == 2 and cur.startswith("-")):
            state["current"] = "0"
        else:
            state["current"] = cur[:-1]
        update_display()

    # ---- Button builder ----
    def make_button(label, bgcolor, color, on_click, data=None, flex=1):
        return ft.Container(
            content=ft.TextButton(
                content=ft.Text(label, size=26, color=color, weight=ft.FontWeight.W_500),
                on_click=on_click,
                data=data if data is not None else label,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=40),
                    overlay_color="#ffffff22",
                ),
            ),
            bgcolor=bgcolor,
            border_radius=40,
            height=70,
            expand=flex,
            alignment=ft.Alignment.CENTER,
        )

    GRAY = "#a5a5a5"
    DARK_GRAY = "#333333"
    ORANGE = "#ff9500"
    BLACK = "#1a1a1a"

    rows = [
        ft.Row(
            controls=[
                make_button("AC", GRAY, "black", on_clear),
                make_button("+/-", GRAY, "black", on_toggle_sign),
                make_button("%", GRAY, "black", on_percent),
                make_button("÷", ORANGE, "white", on_operator, data="÷"),
            ],
            spacing=12,
        ),
        ft.Row(
            controls=[
                make_button("7", DARK_GRAY, "white", on_digit, data="7"),
                make_button("8", DARK_GRAY, "white", on_digit, data="8"),
                make_button("9", DARK_GRAY, "white", on_digit, data="9"),
                make_button("×", ORANGE, "white", on_operator, data="×"),
            ],
            spacing=12,
        ),
        ft.Row(
            controls=[
                make_button("4", DARK_GRAY, "white", on_digit, data="4"),
                make_button("5", DARK_GRAY, "white", on_digit, data="5"),
                make_button("6", DARK_GRAY, "white", on_digit, data="6"),
                make_button("-", ORANGE, "white", on_operator, data="-"),
            ],
            spacing=12,
        ),
        ft.Row(
            controls=[
                make_button("1", DARK_GRAY, "white", on_digit, data="1"),
                make_button("2", DARK_GRAY, "white", on_digit, data="2"),
                make_button("3", DARK_GRAY, "white", on_digit, data="3"),
                make_button("+", ORANGE, "white", on_operator, data="+"),
            ],
            spacing=12,
        ),
        ft.Row(
            controls=[
                make_button("0", DARK_GRAY, "white", on_digit, data="0", flex=2),
                make_button(".", DARK_GRAY, "white", on_decimal),
                make_button("=", ORANGE, "white", on_equals),
            ],
            spacing=12,
        ),
    ]

    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(height=30),
                    ft.Container(
                        content=ft.Column(
                            controls=[expression_text, result_text],
                            horizontal_alignment=ft.CrossAxisAlignment.END,
                            spacing=4,
                        ),
                        padding=ft.Padding.symmetric(horizontal=20),
                        alignment=ft.Alignment.BOTTOM_RIGHT,
                    ),
                    ft.Container(height=20),
                    ft.Column(controls=rows, spacing=12),
                ],
            ),
            padding=ft.Padding.symmetric(horizontal=15, vertical=15),
            bgcolor=BLACK,
            expand=True,
        )
    )


if __name__ == "__main__":
    ft.app(target=main)