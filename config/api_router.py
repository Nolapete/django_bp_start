from rest_framework.routers import DefaultRouter
from apps.users.views import CustomUserViewSet
from apps.products.views import ProductViewSet

# Create a single router to handle all ViewSets
router = DefaultRouter()

# Register the ViewSets with the router
router.register(r"users", CustomUserViewSet, basename="users")
router.register(r"products", ProductViewSet, basename="products")

urlpatterns = router.urls
