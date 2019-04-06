from django.urls import path
from .views import ProfileRetrieveAPIView, \
                   ProfileList

urlpatterns = [
    path(
        'profiles/',
        ProfileList.as_view(),
        name='profile-list'
    ),
    path(
        'profiles/<username>',
        ProfileRetrieveAPIView.as_view(),
        name='profile-detail'
    ),
]
