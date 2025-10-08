# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .api_router import router
from .views import HomeView  # Import the HomeView from config/views.py

if settings.DEBUG:
    import debug_toolbar

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),  # Add this line for the home page
    path("api/", include(router.urls)),
    path("accounts/", include("allauth.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
