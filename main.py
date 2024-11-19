import flet as ft

def main(page: ft.Page):
    page.title = "Менеджер задач"

    tasks = ft.Column()  # Список задач
    task_input = ft.TextField(label="Введите задачу")

    def add_task(e):
        task_row = ft.Row(
            [
                ft.Checkbox(
                    label=task_input.value,
                    on_change=lambda event: update_task(task_row),  # Функция для изменения цвета
                ),
                ft.IconButton(
                    icon=ft.icons.DELETE,
                    on_click=lambda event: remove_task(task_row),
                ),
            ]
        )
        tasks.controls.append(task_row)
        task_input.value = ""  # Очистить поле
        page.update()

    def update_task(task_row: ft.Row):
        checkbox: ft.Checkbox = task_row.controls[0]
        if checkbox.value:  # Если задача выполнена
            print(checkbox.label_style)
            checkbox.label_style = ft.TextStyle(color=ft.colors.GREEN)
        else:  # Если задача не выполнена
            checkbox.label_style.color = None
        page.update()

    def remove_task(task_row):
        tasks.controls.remove(task_row)
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
