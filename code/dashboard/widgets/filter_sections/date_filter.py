import flet as ft
import pandas as pd
import sqlite3
from datetime import datetime, timedelta

from widgets.data_display import DataDisplay

class DateFilter(ft.UserControl):
    def __init__(self):
        super().__init__()
        cnx = sqlite3.connect('temp/articles.db')
        current_date = datetime.now()
        query = "SELECT * FROM articles WHERE"
        for date_index in range(6):
            if date_index ==0:
                query +=" date ='{0}'".format(str((current_date - timedelta(days=date_index)).date()))
            else:
                query +=" or date ='{0}'".format(str((current_date - timedelta(days=date_index)).date()))
        self.fixed_df = pd.read_sql_query(query, cnx)
        self.df = pd.read_sql_query(query, cnx)
        self.status = True

    def filter_date(self, e):
        self.df = self.fixed_df[self.fixed_df['date']== self.select_date_dropdown.value] 
        self.display_card.content = DataDisplay(self.df)
        newspaper_elements = [ft.dropdown.Option(element) for element in self.df['newspaper'].drop_duplicates().sort_values()]
        self.select_newspapers.options = newspaper_elements
        self.update()

    def filter_newspaper(self,e):
        self.df = self.df[self.df['newspaper']== self.select_newspapers.value] 
        print(self.select_newspapers.value)
        self.display_card.content = DataDisplay(self.df)
        self.update()


    def build(self):
        date_elements = [ft.dropdown.Option(element) for element in self.fixed_df['date'].drop_duplicates().sort_values()]
        newspaper_elements = [ft.dropdown.Option(element) for element in self.df['newspaper'].drop_duplicates().sort_values()]
        
        self.select_date_dropdown = ft.Dropdown(
            width=200,
            options=date_elements,
            label='Select Date'
        )
        date_submit = ft.OutlinedButton('Submit',on_click=self.filter_date)
        self.select_newspapers = ft.Dropdown(
            width=700,
            options=newspaper_elements,
            label='Select Title',
        )
        newspaper_submit = ft.OutlinedButton('Submit',on_click=self.filter_newspaper)

        date_section = ft.Column(
            controls=[
                self.select_date_dropdown,
                ft.Container(width=20),
                date_submit,
                ft.Container(width=20)
            ]
        )

        newspaper_section = ft.Column(
            controls=[
                self.select_newspapers,
                ft.Container(width=20),
                newspaper_submit,
                ft.Container(width=20)
            ]
        )


        self.display_card = ft.Card(
            width=1000,
            content=DataDisplay(self.df)
        )
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        [
                            date_section,
                            newspaper_section
                        ]
                    ),
                    self.display_card,
                ],
            )
