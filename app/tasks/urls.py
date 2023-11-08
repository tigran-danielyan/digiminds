from django.urls import path
from tasks.views import TaskViewSet, TaskActionViewSet

urlpatterns = [
    # Transactions
    path('', TaskViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:task_id>/', TaskActionViewSet.as_view({
        'get': 'retrieve',
        'patch': 'update',
        'delete': 'delete',
    }))
]
