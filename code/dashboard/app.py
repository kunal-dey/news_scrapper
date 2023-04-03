import flet as ft

from widgets.filter_sections.date_filter import DateFilter
from widgets.filter_sections.symbol_filter import SymbolFilter
from widgets.stock_app import StockSelectionApp


def main(page:ft.Page):
    page.title = "Stock Selection"
    page.update()

    app = StockSelectionApp()
    
    page.add(
        ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                app,
                DateFilter(),
                SymbolFilter()
            ],
            expand=1,
            scroll=ft.ScrollMode.ADAPTIVE
        ),
    )

ft.app(main)