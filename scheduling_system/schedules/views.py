from django.shortcuts import render
from .models import Event, Technical, Changes
from authentication.models import AppUser
from .serializers import EventSerializer, ChangesSerializer, TechnicalSerializer, DeletedEventSerializer
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .telegram import SmithSegBot
from .telegram import ReadyMessages

# Create your views here.

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):

        serializer.save()

        event_data = serializer.data
        owner_name = AppUser.objects.get(id=event_data.get('owner')).username
        technical_name = Technical.objects.get(id=event_data.get('technical')).name

        created_message = ReadyMessages().created_event_message(
            owner_name,
            event_data.get('title'),
            event_data.get('address'),
            technical_name,
            event_data.get('description'),
            event_data.get('date'),
            event_data.get('start_time'),
            event_data.get('end_time')
        )       

        SmithSegBot.send_message(created_message)

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_destroy(self, instance):

        deleted_event_data = EventSerializer(instance).data
        owner_name = AppUser.objects.get(id=deleted_event_data.get('owner')).username
        technical_name = Technical.objects.get(id=deleted_event_data.get('technical')).name
        deleted_by_name = AppUser.objects.get(id=self.request.user.id).username

        done_message = ReadyMessages().deleted_event_message(deleted_by_name,
                                owner_name,
                                deleted_event_data.get('title'),
                                deleted_event_data.get('address'),
                                technical_name,
                                deleted_event_data.get('description'),
                                deleted_event_data.get('date'),
                                deleted_event_data.get('start_time'),
                                deleted_event_data.get('end_time')
        )

        deleted_data = {
            'owner': deleted_event_data.get('owner'),
            'deleted_by': self.request.user.id,
            'title': deleted_event_data.get('title'),
            'address': deleted_event_data.get('address'),
            'technical': deleted_event_data.get('technical'),
            'description': deleted_event_data.get('description'),
            'date': deleted_event_data.get('date'),
            'start_time': deleted_event_data.get('start_time'),
            'end_time': deleted_event_data.get('end_time'),
        }
        deleted_event_serializer = DeletedEventSerializer(data=deleted_data)
        if deleted_event_serializer.is_valid():
            deleted_event_serializer.save()
        else:
            raise ValueError("Can't save deleted event on database.")

        SmithSegBot.send_admin_message(done_message) 

        instance.delete()

    def perform_update(self, serializer):
        event = self.get_object()
        previous_event = EventSerializer(event).data

        serializer.save()

        current_event = serializer.data

        change_data = {
            'owner': current_event.get('owner'),
            'edited_by': self.request.user.id,

            #old things
            'old_title': previous_event.get('title'),
            'old_address': previous_event.get('address'),
            'old_technical': previous_event.get('technical'),
            'old_description': previous_event.get('description'),
            'old_date': previous_event.get('date'),
            'old_start_time': previous_event.get('start_time'),
            'old_end_time': previous_event.get('end_time'),

            # new things
            'new_title': current_event.get('title'),
            'new_address': current_event.get('address'),
            'new_technical': current_event.get('technical'),
            'new_description': current_event.get('description'),
            'new_date': current_event.get('date'),
            'new_start_time': current_event.get('start_time'),
            'new_end_time': current_event.get('end_time'),
        }

        change_serializer = ChangesSerializer(data=change_data)
        if change_serializer.is_valid():
            change_serializer.save()
        else:
            raise ValidationError("Error on saving change.")

        owner_name = AppUser.objects.get(id=current_event.get('owner')).username
        edited_by_name = AppUser.objects.get(id=self.request.user.id).username
        technical_name = Technical.objects.get(id=current_event.get('technical')).name
        old_technical_name = Technical.objects.get(id=previous_event.get('technical')).name

        done_message = ReadyMessages().edited_event_message(
            owner_name,
            current_event.get('title'),
            current_event.get('address'),
            technical_name,
            current_event.get('description'),
            current_event.get('date'),
            current_event.get('start_time'),
            current_event.get('end_time')
        )

        done_admin_message = ReadyMessages().edited_event_admin_message(
            owner_name,
            edited_by_name,
            previous_event.get('title'),
            previous_event.get('address'),
            old_technical_name,
            previous_event.get('description'),
            previous_event.get('date'),
            previous_event.get('start_time'),
            previous_event.get('end_time'),

            current_event.get('title'),
            current_event.get('address'),
            technical_name,
            current_event.get('description'),
            current_event.get('date'),
            current_event.get('start_time'),
            current_event.get('end_time')
        )

        SmithSegBot.send_message(done_message)
        SmithSegBot.send_admin_message(done_admin_message)
        
class ChangesList(generics.ListAPIView):
    queryset = Changes.objects.all()
    serializer_class = ChangesSerializer

class ChangeDetail(generics.RetrieveAPIView):
    queryset = Changes.objects.all()
    serializer_class = ChangesSerializer

class TechnicalList(generics.ListAPIView):
    queryset = Technical.objects.all()
    serializer_class = TechnicalSerializer

class TechnicalDetail(generics.RetrieveAPIView):
    queryset = Technical.objects.all()
    serializer_class = TechnicalSerializer
