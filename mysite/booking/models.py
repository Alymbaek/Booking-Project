from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class UserProfile(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                           validators=[MinValueValidator(18), MaxValueValidator(100)])
    phone_number = models.PositiveSmallIntegerField()
    STATUS_CHOICES = [
        ('user', 'user'),
        ('owner', 'owner'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='user')

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'


class Region(models.Model):
    region_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.region_name


class Hotel(models.Model):
    region = models.ForeignKey(Region, related_name='hotel', on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=100)
    OT_CHOICES = [
        ('От', 'От')
    ]
    ot = models.CharField(max_length=5, choices=OT_CHOICES, default='От', verbose_name='От')
    price = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='hotel_images/', null=True, blank=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.region}-{self.hotel_name}'

    def get_average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum(review.stars for review in reviews) / reviews.count(), 1)
        return 0


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='room', on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField()
    room = models.IntegerField(choices=[(i, str(i)) for i in range(1, 5)])
    price = models.PositiveSmallIntegerField(default=0)
    STATUS_CHOICES = [
        ('свободен', 'Свободен'),
        ('занят', 'Эанят'),
        ('забронирован ', 'Эабронирован'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.hotel}-{self.number}-{self.room}'


class RoomPhotos(models.Model):
    room = models.ForeignKey(Room, related_name='room_photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='room_photos')


class Review(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    hotel = models.ForeignKey(Hotel, related_name='reviews', on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг', null=True,
                                blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.hotel}-{self.text} -{self.stars}'


class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.room} - {self.check_in}-{self.check_out}'
