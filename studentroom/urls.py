from django.urls import path
from .views import get_room

urlpatterns = [
    # /room/room-number/{any_number}/
    path('room-number/<int:room_id>/', get_room, name='get_room')
]
