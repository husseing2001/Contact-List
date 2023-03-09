from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import permissions


# Create your views here.

class ContactListView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        return Contact.objects.filter(owner=self.request.user)


class ContactDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        return Contact.objects.get(owner=user)
