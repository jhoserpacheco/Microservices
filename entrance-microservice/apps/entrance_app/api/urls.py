from django.urls import path
from .api import ObtainQRView, ConfirmQREntranceView, ConfirmQRExitView, EntranceUserLogs, EntranceGroupLogs

urlpatterns = [
    path('obtain_qr/', ObtainQRView.as_view()),
    path('confirm_entrance/', ConfirmQREntranceView.as_view()),
    path('confirm_exit/', ConfirmQRExitView.as_view()),
    path('logs/user/<user_id>', EntranceUserLogs.as_view()),
    path('logs/group/<group_id>', EntranceGroupLogs.as_view()),
]
