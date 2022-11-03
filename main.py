
import psycopg2 
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

DATABASE_URL = "postgres://wwkgrrgkackczx:6ab9098bb289f8f8f562477a92584b62fe553705f0d846e64a5cafb4aaedbb1b@ec2-3-220-207-90.compute-1.amazonaws.com:5432/dc8sbpl9l91mqf"

def get_url_from_id(url_id):
    con = psycopg2.connect(DATABASE_URL)
    cur = con.cursor()
    cur.execute("SELECT * FROM urls WHERE id='%s'" % url_id)
    id, url = cur.fetchone()
    cur.close()
    con.close()

    return url

app = FastAPI()

@app.get("/s/{url_id}")
async def redirect_to_url(url_id):
  return RedirectResponse(get_url_from_id(url_id))