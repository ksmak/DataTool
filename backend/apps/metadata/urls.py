from django.urls import path
from rest_framework import routers
from .views import (
    DepartmentViewSet,
    DictionaryViewSet,
    DbListView,
    DbStructView,
)


router = routers.SimpleRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'dictionaries', DictionaryViewSet)

urlpatterns = [
    path('db/', DbListView.as_view()),
    path('db/<int:pk>/', DbStructView.as_view()),
]
urlpatterns += router.urls
