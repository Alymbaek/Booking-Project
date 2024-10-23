from django.urls import path
from .views import *
urlpatterns = [
    path('', HotelListViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotel_list'),
    path('<int:pk>/', HotelDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                            'delete': 'destroy'}), name='hotel_list'),

    path('', RoomListViewSet.as_view({'get': 'list', 'post': 'create'}), name='room_list'),
    path('<int:pk/', RoomDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                            'delete': 'destroy'}), name='room_detail'),

    path('', RegionViewSet.as_view({'get': 'list', 'post': 'create'}), name='region_list'),
    path('<int:pk/', RegionViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                            'delete': 'destroy'}), name='region_detail'),

    path('', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('<int:pk/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                            'delete': 'destroy'}), name='review_detail'),


    path('', BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='booking_list'),
    path('<int:pk/', BookingViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                            'delete': 'destroy'}), name='booking_detail'),




    path('', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('<int:pk/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                            'delete': 'destroy'}), name='user_detail'),

]
