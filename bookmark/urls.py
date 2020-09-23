from django.urls import path
from .views import BookMarkListView

urlpatterns = [
    path('', BookMarkListView.as_view(), name='list'),
]