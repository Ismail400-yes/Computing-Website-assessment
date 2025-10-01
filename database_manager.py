import sqlite3 as sql

def listExtension(page=1, no_page=5):
  offset = (page - 1) * no_page
  con = sql.connect("database/data_source.db")
  cur = con.cursor()
  query = """
  SELECT Chat_Image_Link, Title
  FROM "conversation_table"
  WHERE Chat_Image_Link IS NOT NULL AND Chat_Image_Link != ''
  LIMIT ? OFFSET ?
  """
  cur.execute(query, (no_page, offset))
  data = cur.fetchall()
  con.close()
  return [{"image": row[0], "title": row[1]} for row in data]