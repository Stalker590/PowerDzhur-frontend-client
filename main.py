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
            ft.Column(
                [
                    ft.Text("PowerBankDzhur", size=40, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    ft.Text("Якісні павербанки для ваших цілей", size=24, italic=True, color="gray",
                            text_align=ft.TextAlign.CENTER),
                    ft.Divider(height=20, color="transparent"),

                    # Перший рядок - Якість
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.CHECK_CIRCLE, color=ft.Colors.GREEN, size=40),
                            ft.Text("Висока якість продукції, перевірена часом", size=18),
                        ],

                        spacing=15,
                    ),

                    # Другий рядок - Швидка доставка
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.LOCAL_SHIPPING, color=ft.Colors.BLUE, size=40),
                            ft.Text("Швидка доставка по всій Україні", size=18),
                        ],

                        spacing=15,
                    ),

                    # Третій рядок - Вигідна ціна
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.EURO_SYMBOL, color=ft.Colors.ORANGE, size=40),
                            ft.Text("Вигідна ціна та гнучкі умови оплати", size=18),
                        ],

                        spacing=15,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                spacing=20,
            )
        )
        page.update()

    def show_about():
        content.controls.clear()
        content.controls.append(
            ft.Column(
                controls=[
                    ft.Text("Більше про нас", size=36, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    ft.Text(value=show_text, size=10, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            )
        )
        page.update()

    def register():
        # Зберігаємо кожне поле в змінну
        name_field = ft.TextField(width=400, text_align=ft.TextAlign.CENTER)
        surname_field = ft.TextField(width=400, text_align=ft.TextAlign.CENTER)
        email_field = ft.TextField(width=400, text_align=ft.TextAlign.CENTER)
        phone_field = ft.TextField(width=400, text_align=ft.TextAlign.CENTER)

        def show_success_message(msg_text):
            page.snack_bar = ft.SnackBar(
                content=ft.Text(msg_text, color="black"),
                bgcolor="#4CAF50",  # Яскравий зелений
                duration=3000,  # 3 секунди
                show_close_icon=False,
                behavior=ft.SnackBarBehavior.FLOATING
            )
            page.snack_bar.open = True
            page.update()

        # Обробник кнопки підтвердження
        def on_submit(e):
            print("Ім'я:", name_field.value)
            print("Фамілія:", surname_field.value)
            print("Email:", email_field.value)
            print("Телефон:", phone_field.value)
            # Тут можеш додати логіку валідації, відправки на сервер і т.д.

            show_success_message("Успішне підтвердження!")

        # Очищаємо контент
        content.controls.clear()

        # Додаємо все з полями
        content.controls.append(
            ft.Column([
                ft.Text("Реєстрація", size=36, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),

                ft.Row(
                    controls=[ft.Icon(ft.Icons.ACCOUNT_CIRCLE, size=100)],
                    alignment=ft.MainAxisAlignment.CENTER
                ),

                ft.Row([name_field, ft.Text("Вкажіть ім'я", width=150, text_align=ft.TextAlign.CENTER)]),
                ft.Row([surname_field, ft.Text("Вкажіть фамілію", width=150, text_align=ft.TextAlign.CENTER)]),
                ft.Row([email_field, ft.Text("Вкажіть email", width=150, text_align=ft.TextAlign.CENTER)]),
                ft.Row([phone_field, ft.Text("Вкажіть номер телефону", width=150, text_align=ft.TextAlign.CENTER)]),

                ft.ElevatedButton(
                    "Підтвердити",
                    width=150,
                    bgcolor="#4CAF50",
                    color=ft.Colors.BLACK,
                    on_click=on_submit
                )
            ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )

        page.update()

    def account():
        content.controls.clear()
        content.controls.append(
            ft.Column(

                [
                    ft.Text("Аккаунт", size=36, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    ft.Row(  # ось цей ряд — щоб центровано
                        controls=[
                            ft.Icon(ft.Icons.ACCOUNT_CIRCLE, size=100)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton("Авторизуватись", width=150),
                            ft.ElevatedButton("Зареєструватись", width=150, on_click=lambda e: register()),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=30,
                expand=True
            )
        )
        page.update()

    # Створюємо панель навігації з кнопками
    nav = ft.Row(
        [
            ft.ElevatedButton("Головна", on_click=lambda e: show_home()),
            ft.ElevatedButton("Про нас", on_click=lambda e: show_about()),
            ft.ElevatedButton("Ввійти в аккаунт", on_click=lambda e: account()),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    content = ft.Column(expand=True, scroll="auto")

    page.add(nav)
    page.add(content)

    # Показуємо домашню сторінку спочатку
    show_home()


ft.app(
    target=main,
    view=ft.WEB_BROWSER,
    port=8550,
    host="0.0.0.0",
)

