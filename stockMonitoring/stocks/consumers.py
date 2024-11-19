import json
import asyncio
import random
from channels.generic.websocket import AsyncWebsocketConsumer

class StockConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.subscribed_channels = set()  # Track the client's subscriptions
        self.is_sending_data = True       # Control the background data loop
        asyncio.create_task(self.send_stock_data())  # Start data-sending loop

    async def disconnect(self, close_code):
        self.is_sending_data = False  # Stop sending data when client disconnects

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get("action")

        if action == "subscribe":
            channel = data.get("channel")
            if channel:
                self.subscribed_channels.add(channel)
                await self.send(json.dumps({"status": "subscribed", "channel": channel}))

        elif action == "unsubscribe":
            channel = data.get("channel")
            if channel in self.subscribed_channels:
                self.subscribed_channels.remove(channel)
                await self.send(json.dumps({"status": "unsubscribed", "channel": channel}))

    async def send_stock_data(self):
        while self.is_sending_data:
            # Check if the client is subscribed to stock updates
            if "stock_updates" in self.subscribed_channels:
                stock_data = {
                    "AAPL": round(random.uniform(150, 200), 2),
                    "GOOGL": round(random.uniform(2800, 2900), 2),
                    "MSFT": round(random.uniform(300, 350), 2),
                }

                # Send data to the client
                await self.send(json.dumps({"channel": "stock_updates", "data": stock_data}))

            await asyncio.sleep(1)  # Send updates every second

