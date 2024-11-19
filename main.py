import flet as ft

def main(page: ft.Page):
    page.title = "Менеджер задач"

    # Поле ввода
    task_input = ft.TextField(label="Введите задачу")
    
    def add_task(e):
        page.add(ft.Text(task_input.value)) # У текстого поля берем значение
                                            # и добавляем на страницу
        task_input.value = ""  # Очистить поле
        page.update()

    page.add(task_input, ft.ElevatedButton("Добавить задачу", on_click=add_task))

ft.app(target=main)
