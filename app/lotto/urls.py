from django.urls import path

from lotto.views import homepage_view

app_name = 'lotto'

urlpatterns = [
    path('', homepage_view, name='homepage'),
]