from django.db import models

from .agents import Agent

# Create here
class Message(models.Model):
    sender_name = models.CharField(max_length=100)
    message_body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('unread', 'Unread'), ('in_progress', 'In Progress'), ('resolved', 'Resolved')])
    assigned_agent = models.ForeignKey(Agent, null=True, blank=True, on_delete=models.SET_NULL)
    response = models.TextField(blank=True, null=True)