from django.shortcuts import render
from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

def websocket_test(request):
    return render(request, 'contacts/ws_test.html')

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('-created_at')
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        contact = serializer.save()
        self.broadcast_change("created", contact)

    def perform_update(self, serializer):
        contact = serializer.save()
        self.broadcast_change("updated", contact)

    def perform_destroy(self, instance):
        self.broadcast_change("deleted", instance)
        instance.delete()

    def broadcast_change(self, action, contact):
        print(f"[broadcast_change] Action: {action} Contact: {contact.name}")
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "contacts",
            {
                "type": "send_update",
                "message": json.dumps({
                    "action": action,
                    "contact": {
                        "id": contact.id,
                        "name": contact.name,
                        "email": contact.email,
                        "phone": contact.phone,
                    }
                }),
            }
        )
