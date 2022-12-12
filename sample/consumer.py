import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer

class ServerConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.channel_layer = get_channel_layer()
        async_to_sync(self.channel_layer.group_add)(
            "server",
            self.channel_name
        )
        self.send(text_data=json.dumps({
            'message': 'Connected to server'
        }))
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            "server",
            self.channel_name
        )
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.send(text_data=json.dumps({
            'message': message
        }))
        