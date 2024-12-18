import flet as ft
from flet import IconButton, Page, Row, TextField, icons

def main(page: Page):
    page.title = "Flet counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 500
    page.window_height = 700
    page.bgcolor = "WHITE"

    txt_number = TextField(value="0", 
                           text_align=ft.TextAlign.RIGHT,
                           color = "RED", 
                           width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus_click),
                txt_number,
                IconButton(icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
