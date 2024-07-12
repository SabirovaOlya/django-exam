from django.urls import path, include
from .views import ProductListView, LogoutView, RegisterCreateView
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('register', RegisterCreateView.as_view(), name='register_page'),
    path('login', LoginView.as_view(
        template_name='auth/login.html',
        redirect_authenticated_user=True,
        next_page='product_list_page'
    ), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
    path('', ProductListView.as_view(), name='product_list_page'),
    path("ckeditor5/", include('django_ckeditor_5.urls')),

]
