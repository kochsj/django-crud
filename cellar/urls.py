from django.urls import path
from .views import HomePageView, WineDetailView, WineCreateView, WineDeleteView, WineUpdateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), # homepage
    path('cellar/<int:pk>', WineDetailView.as_view(), name='wine_detail'), #detail-view
    path('bottle/new/', WineCreateView.as_view(), name='add_bottle'), #user indicates they want to add something new
    path('delete/<int:pk>', WineDeleteView.as_view(), name='delete_bottle')
]