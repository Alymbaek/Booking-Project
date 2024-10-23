from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'age', 'phone_number', 'status']


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'region_name']



class RegionSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['region_name']

class HotelSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name']

class RoomSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['number']

class ReviewSerializer(serializers.ModelSerializer):
    author = UserProfileSimpleSerializer()
    created_date = serializers.DateTimeField(format='%d-%m-%Y-%H-%M')

    class Meta:
        model = Review
        fields = ['id', 'author', 'text', 'stars', 'created_date']

class RoomPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhotos
        fields = ['image']


class RoomListSerializer(serializers.ModelSerializer):
    room_photos = RoomPhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Room
        fields = ['id', 'number',  'room', 'room_photos', 'price', 'status']


class RoomDetailSerializer(serializers.ModelSerializer):
    room_photos = RoomPhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Room
        fields = ['id', 'room', 'room_photos', 'price', 'status', 'description']


class HotelListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'image', 'average_rating', 'ot', 'price']

    def get_average_rating(self, obj):
        return obj.get_average_rating()

class HotelDetailSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    room = RoomListSerializer(read_only=True, many=True)
    reviews = ReviewSerializer(read_only=True, many=True)
    region = RegionSimpleSerializer()
    owner = UserProfileSimpleSerializer()

    class Meta:
        model = Hotel
        fields = ['id', 'region', 'hotel_name', 'average_rating', 'image', 'description', 'room', 'owner', 'reviews']

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class BookingSerializer(serializers.ModelSerializer):
    hotel = HotelSimpleSerializer()
    room = RoomSimpleSerializer()
    check_in = serializers.DateTimeField(format='%d-%m-%Y-%H-%M')
    check_out = serializers.DateTimeField(format='%d-%m-%Y-%H-%M')


    class Meta:
        model = Booking
        fields = ['hotel', 'room', 'check_in', 'check_out']