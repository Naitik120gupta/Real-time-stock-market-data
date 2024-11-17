import json
import asyncio
import yfinance as yf
from channels.generic.websocket import AsyncWebsocketConsumer

class StockConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.stocks = ['NYKAA.NS','SUZLON.BO','ZOMATO.BO','IRFC.NS']  # Add your stock symbols here
        self.is_running = True
        asyncio.create_task(self.fetch_stock_data())

    async def disconnect(self, close_code):
        self.is_running = False
    async def disconnect(self, close_code):
        self.is_running = False


    async def fetch_stock_data(self):
        while self.is_running:
            stock_data = {}
            for stock in self.stocks:
                ticker = yf.Ticker(stock)
                price = ticker.history(period="1d", interval="1m")['Close'].iloc[-1]
                
                stock_data[stock] = round(price, 2)
            
            await self.send(json.dumps(stock_data))
            await asyncio.sleep(1)  # Update every second

    

    # async def fetch_stock_data(self):
    #     while self.is_running:
    #         stock_data = {}
    #         for stock in self.stocks:
    #             ticker = yf.Ticker(stock)
    #             info = ticker.history(period="1d", interval="1m")[-1:]
    #             stock_data[stock] = {
    #                 "price": info['Close'].values[0],
    #                 "time": info.index[-1].strftime('%Y-%m-%d %H:%M:%S'),
    #             }
    #         await self.send(json.dumps(stock_data))
    #         await asyncio.sleep(5)  # Fetch data every 5 seconds
