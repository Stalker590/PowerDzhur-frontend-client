import flet as ft

def main(page: ft.Page):
    page.title = "Flet Web Server"
    page.theme_mode = 'light'

    page.add(
        ft.Container(  # Ось тут ми додаємо відступи
            content=ft.Column(
                controls=[
                    ft.Text(
                        "PowerBankDzhur",
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Text(
                        "Якісні павербанки для ваших цілей",
                        size=24,
                        italic=True,
                        color="gray",
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Divider(height=20, color="transparent"),
                    ft.Row(
                        [
                            ft.TextField(
                                value="0",
                                width=150,
                                height=60,
                                text_align=ft.TextAlign.CENTER
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                spacing=15
            ),
            padding=20  # Працює тут, у Container
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER, port=8550, host="0.0.0.0")
