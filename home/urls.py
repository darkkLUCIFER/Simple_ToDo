from django.urls import path
from .views import home, todo_detail, todo_delete, todo_create, update_todo

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', todo_detail, name='detail'),
    path('delete/<int:pk>/', todo_delete, name='delete'),
    path('new_todo/', todo_create, name='new_todo'),
    path('update-todo/<int:pk>/', update_todo, name='update_todo'),
]
