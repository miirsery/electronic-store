from os import name
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import LoginForm, LoginView, RegistrationForm, RegistrationView

urlpatterns = [
    # path('', BaseView.as_view(), name='base'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    # path('account/', AccountView.as_view(), name='account'),
    # path('<str:artist_slug>/', ArtistDetailView.as_view(), name='artist_detail'),
    # path('<str:artist_slug>/<str:album_slug>/',
        #  AlbumDetailView.as_view(), name='album_detail'),    
]