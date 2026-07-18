import flet as ft

# flet app structure and setup
def main (page: ft.Page):
    page.title = "Temperature Converter"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 500
    page.window_height = 600
    page.window_resizable = True
    page.padding = 20

    # Input fields for C, F, K
    celcius_input = ft.TextField(
        label = "Celcius C",
        hint_text= "Enter the temperature in celcius",
        keyboard_type= ft.KeyboardType.NUMBER,
        color= ft.Colors.WHITE,
        border_color= ft.Colors.RED,
        on_change=lambda e:convert_from_celcius(e.control.value)            # Implementing the function we made below
    )
    fahrenhiet_input = ft.TextField(
        label = "Fahrenhiet F",
        hint_text= "Enter the temperature in fahrenhiet",
        keyboard_type= ft.KeyboardType.NUMBER,
        color= ft.Colors.WHITE,
        border_color= ft.Colors.RED,
        on_change=lambda e:convert_from_fahrenhiet(e.control.value)         # Implementing the function we made below
    )
    kelvin_input = ft.TextField(
        label = "Kelvin K",
        hint_text= "Enter the temperature in kelvin",
        keyboard_type= ft.KeyboardType.NUMBER,
        color= ft.Colors.WHITE,
        border_color= ft.Colors.RED,
        on_change=lambda e:convert_from_kelvin(e.control.value)             # Implementing the function we made below
    )

    # Add functionality to the app
    def convert_from_celcius(value):
        if value or value.strip:
            try:
                celcius = float(value)
                fahrenhiet = (celcius * 9/5) + 32
                kelvin = celcius + 273.15

                fahrenhiet_input.value = f"{fahrenhiet:.2f}"
                kelvin_input.value = f"{kelvin:.2f}"
                page.update()
            except ValueError:
                celcius_input.value = "ERROR!"
                page.update()
    def convert_from_fahrenhiet(value):
        if value or value.strip:
            try:
                fahrenhiet = float(value)
                celcius = (fahrenhiet - 32) * 5/9
                kelvin = celcius + 273.15

                celcius_input.value = f"{celcius:.2f}"
                kelvin_input.value = f"{kelvin:.2f}"
                page.update()
            except ValueError:
                fahrenhiet_input.value = "ERROR!"
                page.update()
    def convert_from_kelvin(value):
        if value or value.strip:
            try:
                kelvin = float(value)
                celcius = kelvin - 273.15
                fahrenhiet = (celcius * 9/5) + 32

                fahrenhiet_input.value = f"{fahrenhiet:.2f}"
                celcius_input.value = f"{celcius:.2f}"
                page.update()
            except ValueError:
                kelvin_input.value = "ERROR!"
                page.update()
    def clear_all(e):
        celcius_input.value = ""
        fahrenhiet_input.value = ""
        kelvin_input.value = ""
        page.update()

    # Main UI -> Containers
    page.add(
        ft.Column([
            ft.Text(
                "Temperature Converter",
                size= 32,
                weight= ft.FontWeight.BOLD,
                text_align= ft.TextAlign.CENTER,
                color= ft.Colors.BLUE_700
            ),
            ft.Divider(height= 20),
            
            celcius_input,
            ft.Divider(height= 10),
            
            fahrenhiet_input, 
            ft.Divider(height= 10),

            kelvin_input,
            ft.Divider(height= 10),

            ft.ElevatedButton(
                "Clear All",
                icon = ft.Icons.CLEAR,
                style = ft.ButtonStyle(
                    bgcolor = ft.Colors.RED_400,
                    color = ft.Colors.WHITE
                ),
                on_click=clear_all                              # Implementing the function we made below
            ),
            ft.Divider(height=20),

            ft.Container(
                content= ft.Column([
                    ft.Text("Conversion Formulas:", weight= ft.FontWeight.BOLD),
                    ft.Text("• Celsius to Fahrenheit: F = (C x 9/5) + 32"),
                    ft.Text("• Fahrenheit to Celsius: C = (F - 32) x 5/9"),
                    ft.Text("• Celsius to Kelvin: K = C + 273.15"),
                ], spacing=5),
                padding= ft.Padding.all(15),
                border_radius = 10
            )
        ],
        scroll=ft.ScrollMode.AUTO,
        spacing= 0
        )
    )

# Run a flet app
if __name__ == "__main__":
    ft.app(target = main)