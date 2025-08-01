import flet as ft

show_text = """Ми вже давно займаємось справою електронних приладів, і ще з 2016 року зробили багато продаж. Ми розташовуємось у Вінницькій області та маємо хорошу логістику, що дозволяє швидко і якісно доставляти наші товари по всій Україні.

Наш асортимент павербанків ретельно підібраний, щоб відповідати найвищим стандартам якості та надійності. Ми працюємо лише з перевіреними виробниками, тому ви можете бути впевнені, що купуєте справжній продукт, який довго служитиме.

За роки роботи ми здобули довіру тисяч клієнтів, які цінують нашу чесність, оперативність і професійний підхід. Для нас важливо не просто продати товар, а допомогти вам знайти найкраще рішення для ваших потреб — будь то підзарядка в дорозі, на роботі чи вдома.

Наші павербанки відрізняються не лише високою ємністю, а й стильним дизайном, компактністю та зручністю використання. Ви легко зможете взяти їх з собою в подорож, на навчання чи роботу.

Крім того, ми постійно вдосконалюємо сервіс: пропонуємо гарантію, післяпродажну підтримку і можливість обміну товару в разі потреби. Ми цінуємо кожного клієнта і завжди готові вислухати ваші побажання.

Обираючи PowerBankDzhur, ви отримуєте не просто зарядний пристрій — а надійного помічника у будь-якій ситуації. Залишайтеся на зв’язку завжди і скрізь, не переживаючи про розряджений акумулятор.

Запрошуємо вас ознайомитися з нашим каталогом і обрати свій ідеальний павербанк уже сьогодні!"""

def main(page: ft.Page):
    page.title = "PowerDzhur"
    page.theme_mode = 'dark'

    def show_home():
        content.controls.clear()
        content.controls.append(
            ft.Column([
                ft.Text("PowerBankDzhur", size=40, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ft.Text("Якісні павербанки для ваших цілей", size=24, italic=True, color="gray", text_align=ft.TextAlign.CENTER),
                ft.Divider(height=20, color="transparent"),
                ft.Row([
                    ft.TextField(value="0", width=150, height=60, text_align=ft.TextAlign.CENTER),
                ], alignment=ft.MainAxisAlignment.CENTER),
            ], alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True, spacing=15)
        )
        page.update()

    def show_about():
        content.controls.clear()
        content.controls.append(
            ft.Column(
                controls=[
                    ft.Text("Більше про нас", size=36, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    ft.Text(value=show_text, size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            )
        )
        page.update()

    # Створюємо панель навігації з кнопками
    nav = ft.Row(
        [
            ft.ElevatedButton("Головна", on_click=lambda e: show_home()),
            ft.ElevatedButton("Про нас", on_click=lambda e: show_about()),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    content = ft.Column(expand=True,scroll="auto")

    page.add(nav)
    page.add(content)

    # Показуємо домашню сторінку спочатку
    show_home()

ft.app(target=main, view=ft.WEB_BROWSER, port=8550, host="0.0.0.0")
