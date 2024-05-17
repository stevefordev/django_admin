# myproject/urls.py
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhook/', views.receive_alert),
]
