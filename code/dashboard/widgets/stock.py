import flet as ft

class Stock(ft.UserControl):
    def __init__(self, stock_name, priority_name, task_delete):
        super().__init__()
        self.completed = False
        self.stock_name = stock_name
        self.task_delete = task_delete
        self.priority_name = priority_name

    def build(self):
        self.display_stock = ft.Text(self.stock_name)
        self.display_priority = ft.Text(self.priority_name)
        self.edit_stock = ft.TextField(expand=4)
        self.edit_priority = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.display_stock,
                self.display_priority,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.edit_stock,
                ft.Container(width=10),
                self.edit_priority,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )
        return ft.Column(controls=[self.display_view, self.edit_view])
    
    def edit_clicked(self, e):
        self.edit_stock.value = self.display_stock.value
        self.edit_priority.value = self.display_priority.value
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_stock.value = self.edit_stock.value
        self.display_priority.value = self.edit_priority.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def delete_clicked(self, e):
        self.task_delete(self)
