from channels.generic.websocket import AsyncWebsocketConsumer

from django.utils import timezone

import json
import threading

from messaging.models.messages import Chats, Messages
from .commons import bcolors

# Create here
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group = self.scope["url_route"]["kwargs"]["group"]

        # Join room group
        await self.channel_layer.group_add(self.group, self.channel_name)
        await self.accept()


    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.group, self.channel_name)


    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        text = text_data_json["text"]
        sender_id = text_data_json.get("senderId")
        recipient_id = text_data_json.get("recipientId")
        chat_id = text_data_json.get("chatId")

        # Save message thread
        save = SaveMessageThread(text, chat_id, sender_id, recipient_id)
        save.start()
        print(f"{bcolors.OKGREEN} ✓ MESSAGE SAVED!{bcolors.ENDC}")

        # Send message to room group
        await self.channel_layer.group_send(
            self.group, {"type": "chat_message", "text": text}
        )


    # Receive message from room group
    async def chat_message(self, event):
        text = event["text"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"text": text}))


class SaveMessageThread(threading.Thread):
    def __init__(self, text, chat_id, sender_id, recipient_id):
        threading.Thread.__init__(self)
        self.chat_id = chat_id
        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.text = text

    def run(self):
        try:
            chat = Chats.objects.get(id=self.chat_id)
            print(f"{bcolors.OKGREEN} ✓ SUCCESS! CHAT EXISTS{bcolors.ENDC}")
        except Chats.DoesNotExist:
            print(f"{bcolors.WARNING} ✖ CHAT DOES NOT EXIST!{bcolors.FAIL}")

        message = Messages.objects.create(
            sender_type = 'agent',
            sender_id = self.sender_id,
            recipient_id = self.recipient_id,
            chat = chat,
            message_body = self.text,
            timestamp = timezone.now()
        )
        print(f"{bcolors.OKGREEN} ✓ SUCCESS! MESSAGE SAVED!{bcolors.ENDC}")