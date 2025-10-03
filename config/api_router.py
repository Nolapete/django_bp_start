from rest_framework.routers import DefaultRouter
from apps.users.views import CustomUserViewSet
from apps.products.views import ProductViewSet
from apps.tenants.views import TenantViewSet

# Create a single router to handle all ViewSets
router = DefaultRouter()

# Register the ViewSets with the router
router.register(r"users", CustomUserViewSet, basename="users")
router.register(r"products", ProductViewSet, basename="products")
router.register(r"tenants", TenantViewSet, basename="tenants")

urlpatterns = router.urls
