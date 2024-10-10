import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'tasks'  # Define a group name for task notifications

        # Join the group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()  # Accepts the WebSocket connection

    async def disconnect(self, close_code):
        # Leave the group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Called when data is received via WebSocket
        data = json.loads(text_data)
        message = data['message']

        # Send message back to the WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def task_message(self, event):
        # Called when a task message is received from the group
        message = event['message']
        
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
