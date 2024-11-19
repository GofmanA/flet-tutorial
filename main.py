import flet as ft

def main(page: ft.Page):
    page.title = "Менеджер задач"

    tasks = ft.Column()  # Список задач
    task_input = ft.TextField(label="Введите задачу")

    def add_task(e):
        tasks.controls.append(
            ft.Row(
                [
                    ft.Checkbox(label=task_input.value),
                ]
            )
        )
        task_input.value = ""  # Очистить поле
        page.update()

    page.add(task_input, ft.ElevatedButton("Добавить задачу", on_click=add_task), tasks)

ft.app(target=main)
