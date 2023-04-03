import flet as ft
import pandas as pd
from widgets.data_display import DataDisplay
import yfinance as yf
import sqlite3
from datetime import datetime, timedelta

class SymbolFilter(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.stocklist_df = pd.read_csv("temp/EQUITY_NSE.csv").head()
        self.fixed_stocklist_df = pd.read_csv("temp/EQUITY_NSE.csv")
        cnx = sqlite3.connect('temp/articles.db')
        current_date = datetime.now()
        query = "SELECT * FROM articles WHERE"
        for date_index in range(60):
            if date_index ==0:
                query +=" date ='{0}'".format(str((current_date - timedelta(days=date_index)).date()))
            else:
                query +=" or date ='{0}'".format(str((current_date - timedelta(days=date_index)).date()))
        self.fixed_article_df = pd.read_sql_query(query, cnx)
        self.article_df = pd.read_sql_query(query, cnx).head()
    
    def old_article(self,e):
        if self.search_text.value:
            self.article_df = self.fixed_article_df[self.fixed_article_df['title'].str.lower().str.contains(self.search_text.value)]
            self.article_df = self.article_df.sort_values(by=['date'])
            self.stocklist_df = self.fixed_stocklist_df[self.fixed_stocklist_df['Company Name'].str.lower().str.contains(self.search_text.value)]
            self.display_columns.controls[0] = DataDisplay(self.article_df)
            self.display_columns.controls[1] = DataDisplay(self.stocklist_df)
            self.update()

    def returns(self,e):
        if self.symbol_return.value:
            fin_article_df = yf.download(tickers=f'{self.symbol_return.value}.NS',period='1mo',interval='1d').pct_change()+1
            fin_article_df['date'] = fin_article_df.index
            fin_article_df = fin_article_df[['Close','date']]
            self.returns_section.controls[3] =DataDisplay(fin_article_df)
            self.update()


    def build(self):
        fin_article_df = yf.download(tickers='TCS.NS',period='1mo',interval='1d').pct_change()+1
        fin_article_df['date'] = fin_article_df.index
        fin_article_df = fin_article_df[['Close','date']].tail()

        self.search_text = ft.TextField(
            hint_text="Text to search",
            width=200
        )
        symbol_submit = ft.OutlinedButton('Submit',on_click=self.old_article)

        old_article_section = ft.Column(
            controls=[
                self.search_text,
                ft.Container(width=20),
                symbol_submit
            ]
        )
        self.display_columns = ft.Column(
                [DataDisplay(self.article_df),DataDisplay(self.stocklist_df)]
            )
        display_card = ft.Card(
            width=1000,
            content= self.display_columns
        )
        self.symbol_return = ft.TextField(
            hint_text="Symbol to search",
            width=200
        )
        return_submit = ft.OutlinedButton('Submit',on_click=self.returns)
        

        self.returns_section = ft.Column(
            controls=[
                self.symbol_return,
                ft.Container(width=20),
               return_submit,
               DataDisplay(fin_article_df)
            ]
        )
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    old_article_section,
                    display_card,
                    self.returns_section
                ],
                expand=1,
                scroll=ft.ScrollMode.ADAPTIVE
            )
