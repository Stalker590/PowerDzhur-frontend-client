import flet as ft

def main(page: ft.Page):
    page.title = "Flet Web Server"
    page.add(ft.Text("Привіт, братику! Це веб-сервер на Flet."))

ft.app(target=main, view=ft.WEB_BROWSER, port=8550, host="0.0.0.0")
