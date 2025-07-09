from django.contrib import admin
from django.urls import path
from bot.views import register_user, get_user_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', register_user),
    path('api/user/<int:userId>/', get_user_info),  # Совпадает с параметром в `views.py`
]
