from django.urls import path
from rest_framework import routers
from .views import (
    DictionaryViewSet,
    DatabaseViewSet,
    GenerateView
)

router = routers.SimpleRouter()
router.register(r'dictionaries', DictionaryViewSet)
router.register(r'databases', DatabaseViewSet)

urlpatterns = [
    path('generate_db', GenerateView.as_view())
]

urlpatterns += router.urls
