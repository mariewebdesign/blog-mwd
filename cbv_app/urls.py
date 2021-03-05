from django.urls import path
from cbv_app import views

app_name = 'cbv_app'

urlpatterns = [
    path('',views.CBView.as_view(),name='index'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('shop_list/',views.ShopListView.as_view(),name='shop_list'),
    path('shop_list/<int:pk>/',views.ShopDetailsView.as_view(),name="shop_detail"),
    path('create/',views.ShopCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.ShopUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.ShopDeleteView.as_view(),name='delete'),
]