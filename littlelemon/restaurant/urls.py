from django.urls import path, include

from .views import BookingViewSet, MenuItemsView, SingleMenuItemView # , menuView not required

urlpatterns = [
    # path('booking/', BookingView.as_view(), name='booking_view'),
    # path('menu/', MenuView.as_view(), name='menu_view'), not required
    path('items/', MenuItemsView.as_view()),
    path('items/<int:pk>', SingleMenuItemView.as_view()),
]
