
from django.urls import path
from .views import (
    NotificationListAPIView,
    UnreadCountAPIView,
    MarkNotificationReadAPIView,
    MarkAllReadAPIView
)

urlpatterns = [
    path('', NotificationListAPIView.as_view(), name='notifications-list'),
    path('unread-count/', UnreadCountAPIView.as_view(), name='notifications-unread-count'),
    path('<int:pk>/mark-read/', MarkNotificationReadAPIView.as_view(), name='notification-mark-read'),
    path('mark-all-read/', MarkAllReadAPIView.as_view(), name='notifications-mark-all-read'),
]
