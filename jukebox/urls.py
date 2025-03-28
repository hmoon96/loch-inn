from . import views
from django.urls import path

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("", views.search, name="index"),
    path("search/", views.search, name="search"),
    path('add-to-local-list/<int:embed_id>/', views.add_to_local_list, name='add_to_local_list'),
]
