import flet as ft

def main(page: ft.Page):
    page.title = "Менеджер задач"
    page.add(ft.Text("Добро пожаловать в менеджер задач!"))

ft.app(target=main)
