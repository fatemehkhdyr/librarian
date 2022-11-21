from django.urls import path
from .views import signup, signin, logout_view, signup_librarian

app_name = "account"

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', signin, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup_librarian', signup_librarian, name='signup_librarian')
]