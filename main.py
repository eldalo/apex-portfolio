from fastapi import FastAPI
from controllers import router as portfolio_router

app = FastAPI()

app.include_router(portfolio_router, tags=["Portfolios"], prefix="")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3002)
