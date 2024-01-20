from django.db import models

from .agents import Agent

# Create here
class Customer(models.Model):
    full_name = models.CharField(max_length=100, blank=True, null=True)


class Chats(models.Model):
    sender = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='chat_sender')
    date_created = models.DateTimeField(auto_now_add=True)

    @property
    def messages(self):
        return self.chat_messages.all()
    
    class Meta:
        ordering = ['-date_created']



class Message(models.Model):
    SENDER_TYPES = (
        ('customer', 'Customer'),
        ('agent', 'Agent'),
    )

    sender_type = models.CharField(max_length=10, choices=SENDER_TYPES, default='customer', null=True)
    sender = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='message_sender', null=True)
    recipient = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='message_recipient', null=True)
    chat = models.ForeignKey(Chats, on_delete=models.CASCADE, related_name='chat_messages', null=True)
    message_body = models.TextField()
    timestamp = models.DateTimeField(null=True)
    assigned_agent = models.ForeignKey(Agent, null=True, blank=True, on_delete=models.SET_NULL)
    response = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-timestamp']