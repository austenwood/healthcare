from django.urls import path
from .views import (
    MemberListApiView,
    UploadFileView
)

urlpatterns = [
    path('members/', MemberListApiView.as_view()),
    path('upload/', UploadFileView.as_view(), name='upload-file')
]