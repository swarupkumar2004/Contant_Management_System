import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ContactConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("contacts", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("contacts", self.channel_name)

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            "contacts",
            {
                "type": "send_update",
                "message": text_data,
            }
        )

    async def send_update(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"]
        }))
