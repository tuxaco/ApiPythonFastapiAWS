from fastapi import APIRouter
import requests

router = APIRouter()


@router.get("/news")
async def get_news():
    """ Get market news:
    * It shows the latest market news"""
    r = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    data = r.json()
    news = data['Data']
    return news
