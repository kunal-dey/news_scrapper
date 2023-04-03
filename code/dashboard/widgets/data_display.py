import flet as ft

class DataDisplay(ft.UserControl):
    def __init__(self, df):
        super().__init__()
        self.df = df

    def build(self):
        data_columns_head = []
    
        for column in list(self.df.columns):
            data_columns_head.append(ft.DataColumn(ft.Text(f"{column}")))

        self.data_rows=[]

        for index in range(self.df.shape[0]):
            row = self.df.iloc[index]
            columns_length = self.df.shape[1]
            self.data_rows.append(
                ft.DataRow(
                        cells= [ft.DataCell(ft.Text(row.iloc[i])) for i in range(columns_length)]
                        # [
                        #     ft.DataCell(ft.Text(row.iloc[0])), # date
                        #     ft.DataCell(ft.Text(row.iloc[1])), # company_symbol
                        #     ft.DataCell(ft.Text(row.iloc[2])), # title
                        # ]
                )
            )
        return ft.DataTable(
            columns=data_columns_head,
            rows=self.data_rows
        )
