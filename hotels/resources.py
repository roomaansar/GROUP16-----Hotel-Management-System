from import_export import resources
from .models import Room, Booking, Transaction

class RoomResource(resources.ModelResource):
    class Meta:
        model = Room

class BookingResource(resources.ModelResource):
    class Meta:
        model = Booking

class TransactionResource(resources.ModelResource):
    class Meta:
        model = Transaction
        