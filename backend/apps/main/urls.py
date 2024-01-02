from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'documents', DocumentsViewSet)
router.register(r'countries', CountriesViewSet)
router.register(r'nationals', NationalsViewSet)
router.register(r'registrationstate', RegistrationstateViewSet)
router.register(r'asb', AsbViewSet)
router.register(r'address', AddressViewSet)

urlpatterns = router.urls

