from django.urls import path, include
from .views import (
    MemberListApiView,
)

urlpatterns = [
    path('members/', MemberListApiView.as_view()),
]