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

    def clear_tasks(e):
        tasks.controls.clear()
        page.update()

    page.add(
        task_input,
        ft.ElevatedButton("Добавить задачу", on_click=add_task),
        tasks,
        ft.ElevatedButton("Очистить задачи", on_click=clear_tasks)
    )

ft.app(target=main)
