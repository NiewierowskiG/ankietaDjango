from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_view),
    path('create', views.create_ankieta),
    path('<int:id>', views.update_ankieta),
    path('delete/<int:id>', views.delete_ankieta)
]