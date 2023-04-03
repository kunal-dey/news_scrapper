import sqlite3

class NewsscrapPipeline:

    def __init__(self) -> None:
        self.create_connection()
        try:
          self.create_table()
        except:
           pass

    def create_connection(self):
        self.conn = sqlite3.connect("../../dashboard/temp/articles.db")
        self.cursor = self.conn.cursor()

    def create_table(self):     
        self.cursor.execute(
            '''CREATE TABLE articles (
                title TEXT,
                newspaper INTEGER,
                date TEXT
            )
            '''
        )
        
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self,item):
        self.cursor.execute('''SELECT title FROM articles WHERE title = ? and date = ?''',(item['title'],item['date']))
        result = self.cursor.fetchone()
        if result is None:
            insert_query='''INSERT INTO articles (title, newspaper, date)
            VALUES (?, ?, ?)
            '''
            self.cursor.execute(insert_query,(item['title'],item['newspaper'], item['date']))
            self.conn.commit()
    

