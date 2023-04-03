"""
    This transformation removes all backdated news from the table
"""
import sqlite3
from datetime import datetime, timedelta

DAYS_TO_HOLD = 60

def main():
    global DAYS_TO_HOLD
    conn = sqlite3.connect("../dashboard/temp/articles.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT min(date) FROM articles''')

    drop_query = "DELETE FROM articles WHERE"
    oldest_date = cursor.fetchone()[0]
    print(oldest_date)
    # start_date = datetime.strptime(oldest_date, '%Y-%m-%d')
    # end_date = datetime.now() - timedelta(days=DAYS_TO_HOLD) # here end date is recent date
    # while start_date <= end_date:
    #     drop_query += " date = '{0}' or".format(start_date.strftime('%Y-%m-%d'))
    #     start_date += timedelta(days=1)

    # cursor.execute(drop_query[:-3])
    # conn.commit()
    # conn.close()
    

if __name__ == '__main__':
    main()