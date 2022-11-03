
import psycopg2
import random 
import string

from fastapi import FastAPI 
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

DATABASE_URL = "postgres://wwkgrrgkackczx:6ab9098bb289f8f8f562477a92584b62fe553705f0d846e64a5cafb4aaedbb1b@ec2-3-220-207-90.compute-1.amazonaws.com:5432/dc8sbpl9l91mqf"


def get_url_from_id(url_id):
  con = psycopg2.connect(DATABASE_URL)
  cur = con.cursor()
  cur.execute("SELECT * FROM urls WHERE id='%s'" % url_id)
  
  id, url = cur.fetchone()
  cur.close()
  con.close()
  
  return url
  
def get_shortened_url(url):
  con = psycopg2.connect(DATABASE_URL)
  cur = con.cursor()
  random_id = ''.join(random.choice(string.ascii_letters) for i in range(6))
  
  cur.execute("INSERT INTO urls (id, url) VALUES('%s', '%s');" % (random_id, url))
  con.commit()
  cur.close()
  con.close()
  return random_id
  
class UrlData(BaseModel):
  url: str
  
app = FastAPI()
  
@app.get("/s/{url_id}")
async def redirect_to_url(url_id):
  return RedirectResponse(get_url_from_id(url_id))
  
@app.post("/shorten-url")
async def root(data: UrlData):
  url = data.url
  return {"id": get_shortened_url(url)}