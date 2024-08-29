from fastapi import APIRouter, HTTPException, status
from typing import List
from models import Portfolio, portfolio_helper
from database import portfolio_collection
from bson import ObjectId

router = APIRouter()

@router.get("/portfolios", response_model=List[Portfolio])
async def get_portfolios(clientId: str):
    portfolios = await portfolio_collection.find({"customerCode": clientId}).to_list(100)
    return [portfolio_helper(portfolio) for portfolio in portfolios]

@router.get("/portfolios/{id}", response_model=Portfolio)
async def get_portfolio(id: str):
    portfolio = await portfolio_collection.find_one({"_id": ObjectId(id)})
    if portfolio is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Portfolio not found")
    return portfolio_helper(portfolio)
