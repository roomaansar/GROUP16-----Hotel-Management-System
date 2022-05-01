"""RoomManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import HotelList, HotelDetail, RoomList, RoomDetail, search, BookingList, BookingDetail, BookingCreate, emailView, about, print_report

app_name = "hotels"

urlpatterns = [
    path('', HotelList.as_view(), name='hotel-list'),
    path('<int:pk>', HotelDetail.as_view(), name='hotel-detail'),
    path('search/', search, name='search'),
    path('<int:hotel_pk>/rooms', RoomList.as_view(), name='room-list'),
    path('<int:hotel_pk>/rooms/<int:pk>', RoomDetail.as_view(), name='room-detail'),
    path('bookings/', BookingList.as_view(), name='bookings'),
    path('bookings/<int:pk>', BookingDetail.as_view(), name='booking-detail'),
    path('booking/', BookingCreate.as_view(), name='booking-create'),
    path('email/', emailView, name='email'),
    path('about/', about, name='about'),
    path('print/', print_report, name='print'),
]
