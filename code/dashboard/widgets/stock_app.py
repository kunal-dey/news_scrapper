import flet as ft
import requests

from widgets.stock import Stock

class StockSelectionApp(ft.UserControl):

    def submit_requests(self, e):
        payload = {}
        for stock in self.stocks.controls:
            payload[stock.stock_name] = stock.priority_name
        # requests.post("http://127.0.0.1:8080/stocks",data= payload).json()
        self.stocks.controls = []
        self.update()

    def add_clicked(self,e):
        if self.new_stock.value and self.priority.value:
            stock = Stock(self.new_stock.value, self.priority.value,self.task_delete)
            self.stocks.controls.append(stock)
            self.new_stock.value = ""
            self.priority.value = ""
            self.new_stock.focus()
            self.update()

    def clear_clicked(self, e):
        self.stocks.controls = []
        self.update()

    def build(self):
        self.new_stock = ft.TextField(
            hint_text="Enter stock symbol",
            expand=True
        )
        self.priority = ft.TextField(
            hint_text="Enter stock rank",
            width=150
        )
        self.stocks = ft.Column()
        self.stocks_selected = ft.Text("0 stocks selected")

        return ft.Card(
            content=ft.Container(
                padding=10,
                content=ft.Column(
                    width=1000,
                    controls=[
                        ft.Row([ft.Text(value="Todos", style="headlineMedium")], alignment="center"),
                        ft.Row([
                            self.new_stock,
                            self.priority,
                            ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked)
                        ],spacing=10),
                        ft.Column(
                            spacing=25,
                            controls=[
                                self.stocks,
                                ft.Row(
                                    alignment="spaceBetween",
                                    vertical_alignment="center",
                                    controls=[
                                        self.stocks_selected,
                                        ft.Row(
                                            controls=[
                                                ft.OutlinedButton(
                                                    text="Submit all stocks selected", on_click=self.submit_requests
                                                ),
                                                ft.Container(width=10),
                                                ft.OutlinedButton(
                                                    text="Clear to start again", on_click=self.clear_clicked
                                                ),
                                            ]
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ]
                )
            )
        )

    def task_delete(self, task):
        self.stocks.controls.remove(task)
        self.update()

    def update(self):
        self.stocks_selected.value = f"{len(self.stocks.controls)} active item(s) selected"
        super().update()
