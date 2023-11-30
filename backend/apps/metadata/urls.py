from django.urls import path
from rest_framework import routers
from .views import (
    DepartmentViewSet,
    DictionaryViewSet,
    DatabaseViewSet
)


router = routers.SimpleRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'dictionaries', DictionaryViewSet)
router.register(r'databases', DatabaseViewSet)

urlpatterns = router.urls
