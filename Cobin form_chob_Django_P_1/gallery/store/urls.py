from django.urls import path
from . import views
from .views import robots_txt

urlpatterns = [
    path('', views.StoreView.as_view(), name='store'),
    path('order/', views.OrderView.as_view(), name='order'),
    path('order/success/', views.OrderSuccessView.as_view(), name='order_success'),
    path('contact/', views.MessageCreateView.as_view(), name='message_create'),
    path("robots.txt", robots_txt, name="robots_txt"),
    path('category/<slug:category_slug>/', views.CategoryDetailView.as_view(), name='category_detail'),

]