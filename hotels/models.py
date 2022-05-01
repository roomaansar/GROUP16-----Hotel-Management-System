from django.db import models, transaction
from django.urls import reverse
from django.core.mail import EmailMessage
from RoomManagementSystem.emails import BOOKING_EMAIL

# Create your models here.

class Hotel(models.Model):
    """Model definition for Hotel."""

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    address = models.TextField(default="Address")
    contact = models.CharField(max_length=100, default='123456789')
    email = models.EmailField(max_length=100, default='hotel_name@email.com')
    rating = models.DecimalField(decimal_places=2, max_digits=4, default=3)
    num_rating = models.PositiveIntegerField(default=0)
    wallet = models.IntegerField(default=100)

    def get_absolute_url(self):
        """Return absolute url for Hotel."""
        return reverse('hotels:hotel-detail', args=[str(self.pk)])

    def __str__(self):
        """Unicode representation of Hotel."""
        return str(self.name) + '(' + str(self.location) + ')'
class Room(models.Model):
    """Model definition for Room."""

    OCCUPANCY_CHOICES = [
        ("SINGLE", "SINGLE"),
        ("DOUBLE", "DOUBLE"),
    ]
    TYPE_CHOICES = [
        ("A/C(Air Conditioned)", "A/C(Air Conditioned)"),
        ("Non A/C(Non Air Conditioned)", "Non A/C(Non Air Conditioned)"),
    ]

    hotel = models.ForeignKey('hotels.Hotel', on_delete=models.CASCADE)
    type_name = models.CharField(max_length=100, default="Deluxe")
    occupancy = models.CharField(max_length=50, choices=OCCUPANCY_CHOICES , default="SINGLE")
    room_type = models.CharField(max_length=50, choices=TYPE_CHOICES , default="Non A/C(Non Air Conditioned)")
    maximum = models.PositiveIntegerField(default=10)
    available = models.PositiveIntegerField(default=10)
    cost = models.PositiveIntegerField(default=1000)

    def get_absolute_url(self):
        """Return absolute url for Room."""
        return reverse('hotels:room-detail', args=[str(self.hotel.pk), str(self.pk)])

    def __str__(self):
        """Unicode representation of Room."""
        return str(self.hotel) + ': ' + str(self.type_name) + ': ' + str(self.occupancy) + ': ' + str(self.room_type)

class Transaction(models.Model):
    """Model definition for Transaction."""
    
    from_user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    to_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField()
    reason = models.CharField(max_length=100)
    success = models.BooleanField(default=False)

    def send_email(self, transaction):
        try:
            subject = "Invoice for Transaction %d" % transaction.id
            body = BOOKING_EMAIL % (transaction.from_user.username, transaction.id, transaction.from_user.username, transaction.to_hotel, transaction.amount, transaction.time, transaction.success)
            email = EmailMessage(subject, body, to=[transaction.from_user.email])
            email.send()
        except Exception as e:
            print("%s\nUnable to send email to %s" % (e, transaction.from_user.email))

    @transaction.atomic
    def make_transaction(self,from_user, to_hotel, amount, reason):
        status = False
        if from_user.wallet >= amount:
            from_user.wallet -= amount
            to_hotel.wallet += amount
            from_user.save()
            to_hotel.save()
            status = True
        transaction = Transaction(from_user=from_user.user, to_hotel=to_hotel, amount=amount, success=status, reason=reason)
        transaction.save()
        self.send_email(transaction)
        return transaction, status


    def __str__(self):
        """Unicode representation of Transaction."""
        return str(self.id) + ': ' + str(self.from_user) + ' to ' + str(self.to_hotel)\
               + ' - ' + str(self.amount)

class Booking(models.Model):
    """Model definition for Booking."""
    
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    customer = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    room = models.ForeignKey('hotels.Room', on_delete=models.CASCADE)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    num_rooms = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    user_rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Unicode representation of Booking."""
        return str(self.room.pk) + ' ' + str(self.num_rooms)
