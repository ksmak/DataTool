from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'documents', DocumentsViewSet)
router.register(r'country', CountryViewSet)
router.register(r'asb', AsbViewSet)

urlpatterns = router.urls

