from django.urls import path, include
from rest_framework import routers
from api.views import ColonneViewset, TaskViewset, BoardView

router = routers.DefaultRouter()
router.register(r'col', ColonneViewset)
router.register(r'task', TaskViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('board', BoardView.as_view()),
]