from django.contrib import admin
from django.urls import path, include
from member_api import urls as member_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('members/', include(member_urls)),
]