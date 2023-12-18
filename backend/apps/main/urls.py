from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'documents', DocumentsViewSet)
router.register(r'region', RegionViewSet)
router.register(r'address', AddressViewSet)
router.register(r'asb', AsbViewSet)

urlpatterns = router.urls

