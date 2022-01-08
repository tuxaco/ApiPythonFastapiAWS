from fastapi import APIRouter
from .endpoints import trading, prices, news

router = APIRouter()
router.include_router(trading.router, tags=["Trading Signals"])
router.include_router(prices.router, tags=["Prices"])
router.include_router(news.router, tags=["News"])
