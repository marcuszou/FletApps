# -*- coding: utf-8 -*-
"""
@author: Marcus Zou
"""

import flet as ft

def main(page: ft.Page):

    def addTask(p):
        checkBox = ft.Checkbox(value=False)
        checkBoxText = ft.Text(value=textField.value, width=350, bgcolor="WHITE", size=16)
        taskRow = ft.Row(controls=[checkBox, checkBoxText], alignment=ft.MainAxisAlignment.START)
        page.add(taskRow)

    ## Window Size
    page.title = "Tasking App by AlfaZen"
    page.window_width = 500
    page.window_height = 700
    page.bgcolor = "WHITE"  ## Go to colothunt.co to pick up the colors

    ## Add widgets
    textField = ft.TextField(width=400)
    addBtn = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=addTask)
    entriesRow = ft.Row(controls=[textField, addBtn], 
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    #checkBox = ft.Checkbox(value=True)
    #checkBoxText = ft.Text(value="Task 1", width=350, bgcolor="WHITE", size=16)

    page.add(entriesRow)

## Desktop app
ft.app(target=main)
## Web App
# ft.app(target=main, view=ft.WEB_BROWSER)
