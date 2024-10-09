from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_user, name='create'),
    path('users_list/', views.users_list, name='users_list'),
    path('user_detail/<str:username>', views.user_detail, name='user_detail'),
    path('update_user/<str:username>', views.update_user, name='update_user'),
    path('update_user_details/<str:username>', views.update_user_details, name='update_user_details'),
    path('delete_user/<str:username>', views.delete_user, name='delete_user')
]
