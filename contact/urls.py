from django.urls import path
from contact import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id>/', views.contact, name='contact')
]