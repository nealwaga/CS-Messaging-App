from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from messaging.models.messages import Customers, Chats, Messages

# Create here
class ChatsView(LoginRequiredMixin, View):
    template_name = 'messaging/chats.html'

    def get(self, request):
        recipients = Customers.objects.all()

        pk = self.request.GET.get('pk')
        if "action" in request.GET.keys():
            action = request.GET["action"]
            if action == "get_chats":
                customers = Customers.objects.filter(id=pk).first()

                chat_data = []
                for chat in customers.chat_sender.all():
                    chat_messages = [
                        {"pk": message.pk, "message": message.message_body, "sender_type":message.sender_type, 
                            "date_created":message.timestamp.strftime('%I:%M %p, %B %d, %Y'), 
                        } for message in chat.chat_messages.all()
                    ]
                    chat_data.append({
                        "pk": chat.pk,
                        "messages": chat_messages,
                        "chat_id": chat.pk
                    })
                
                return JsonResponse({"chats": chat_data, "customer": customers.full_name, "ID": customers.id,}, 
                                    safe=False)

        context = {
            'recipients': recipients,
        }
        return render(request, self.template_name, context)