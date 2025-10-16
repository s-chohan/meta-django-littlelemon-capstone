from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from . import views # import BookingViewSet, MenuItemsView, SingleMenuItemView # , menuView not required

urlpatterns = [
    # path('booking/', BookingView.as_view(), name='booking_view'),
    # path('menu/', MenuView.as_view(), name='menu_view'), not required
    path('items/', views.MenuItemsView.as_view()),
    path('items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]
