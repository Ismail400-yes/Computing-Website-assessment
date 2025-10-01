import sqlite3 as sql

def listExtension():
  con = sql.connect("database/data_source.db")
  cur = con.cursor()
  data = cur.execute("SELECT Chat_Image_Link, Title FROM conversation_table").fetchall()
  con.close()
  return data