import flet as ft 

#flet app structure and setup
def sach(page: ft.Page):
    page.title="Temperature converter"
    page.theme_mode=ft.ThemeMode.DARK
    page.window_width=500
    page.window_height=600
    page.window_resizable=True
    page.padding=20

    # Input field for C ,F ,K
    celsius_input=ft.TextField(
        label="Celsius",
        hint_text="Enter temperature in Celsius",
        keyboard_type=ft.KeyboardType.NUMBER,
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        on_change=lambda e: convert_to_celsius(e.control.value)

    )

    fahrenheit_input=ft.TextField(
        label="Fahrenheit",
        hint_text="Enter temperature in Fahrenheit",
        keyboard_type=ft.KeyboardType.NUMBER,
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        on_change=lambda e: convert_to_fahrenheit(e.control.value)

    )

    kelvin_input=ft.TextField(
        label="Kelvin",
        hint_text="Enter temperature in Kelvin",
        keyboard_type=ft.KeyboardType.NUMBER,
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        on_change=lambda e: convert_to_kelvin(e.control.value)

    )

    # Add functionality to the App
    def convert_to_celsius(value):
        if value and value.strip():
            try:
                celsius = float(value)
                fahrenheit = (celsius * 9/5) + 32
                kelvin = celsius + 273.15

                fahrenheit_input.value = f"{fahrenheit:.2f}"
                kelvin_input.value = f"{kelvin:.2f}"
                page.update()
            except ValueError:
                celsius_input.value= f"ERROR!"

    def convert_to_fahrenheit(value):
        if value and value.strip():
            try:
                fahrenheit = float(value)
                celsius = (fahrenheit - 32) * 5/9
                kelvin = celsius + 273.15

                celsius_input.value = f"{celsius:.2f}"
                kelvin_input.value = f"{kelvin:.2f}"
                page.update()
            except ValueError:
                fahrenheit_input.value= f"ERROR!"

    def convert_to_kelvin(value):            
        if value and value.strip():
            try:
                kelvin = float(value)
                celsius = kelvin - 273.15
                fahrenheit = (celsius * 9/5) + 32

                celsius_input.value = f"{celsius:.2f}"
                fahrenheit_input.value = f"{fahrenheit:.2f}"
                page.update()
            except ValueError:
                kelvin_input.value= f"ERROR!"   

    def cleaer_all(e):
        celsius_input.value=""
        fahrenheit_input.value=""
        kelvin_input.value=""
        page.update()





    # Create the main UI --> containers
    page.add(
        ft.Column([
            ft.Text(
                "Temperature Converter",
                size=28,
                weight = ft.FontWeight.BOLD,
                text_align = ft.TextAlign.CENTER,
                color = ft.Colors.AMBER_200
            ),
            ft.Divider(height=20),

            celsius_input,
            ft.Divider(height=10),

            fahrenheit_input,
            ft.Divider(height=10),

            kelvin_input,
            ft.Divider(height=20),

            ft.ElevatedButton(
                "Clear All",
                on_click=cleaer_all,
                icon=ft.Icons.CLEAR,
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.RED_400,
                    color=ft.Colors.WHITE
                )
            ),

            ft.Divider(height=20),

            ft.Container(
                content=ft.Column([
                    ft.Text("Conversion Formula :" , weight=ft.FontWeight.BOLD),
                    ft.Text("Celsius to Fahrenheit :F = (C × 9/5 + 32)"),
                    ft.Text("Fahrenheit to Celsius : C = (F - 32) × 5/9"),
                    ft.Text("Kelvin to Celsius : C = K - 273.15"),
                ], spacing=5),
                padding=15,
                border_radius= 10
            

            )


        ], 
        scroll=ft.ScrollMode.AUTO,
        spacing=0
        )

    )


#run
if __name__ =="__main__":
    ft.app(target=sach)