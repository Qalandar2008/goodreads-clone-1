from django.contrib.auth.views import LogoutView
from django.urls import path, include
from users.views import RegisterView, LoginView, ProfileView, ProfileEditView

urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile' ),
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
]