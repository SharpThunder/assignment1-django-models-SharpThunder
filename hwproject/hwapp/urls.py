from django.conf.urls import url
from hwapp import views
urlpatterns = [
    url(r'^singerpage/', views.index, name='singerpage'),
    ]