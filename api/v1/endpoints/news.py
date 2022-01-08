from fastapi import APIRouter
import requests

router = APIRouter()


@router.get("/news")
async def get_news():
    """ Get market sentiment:
    * if bullish, prices are expected to rise - optimistic
    * if bearish, prices are expected to fall - pessimistic """
    r = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    data = r.json()
    news = data['Data']
    return news
