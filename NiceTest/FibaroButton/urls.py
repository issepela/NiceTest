from django.urls import path
from . import views


app_name='FibaroButton'
urlpatterns = [
    path('', views.NicetestListView.as_view(), name='all'),
    path('add/', views.AddView.as_view(), name='add'),
    path('status/', views.Nicetestbuttonstatus, name='button status'),
]