import json
from channels.generic.websocket import AsyncWebsocketConsumer
import datetime
import yfinance as yf
import asyncio

class StockConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.subsrcribed = False
        await self.send(text_data=json.dumps({
            'message': 'Hello there! '
        }))

# class StockConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_group_name = "stocks"
#         await self.channel_layer.group_add(self.room_group_name, self.channel_name)
#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         stock_symbol = data['symbol']
#         price = data['price']

#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'send_stock_update',
#                 'symbol': stock_symbol,
#                 'price': price
#             }
#         )

#     async def send_stock_update(self, event):
#         symbol = event['symbol']
#         price = event['price']

#         await self.send(text_data=json.dumps({
#             'symbol': symbol,
#             'price': price
#         }))


