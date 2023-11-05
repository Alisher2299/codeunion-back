from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

Router = DefaultRouter if settings.DEBUG else SimpleRouter
router = Router(trailing_slash=settings.APPEND_SLASH)

urlpatterns = [
    path(route="api/users/", view=include(arg="users.urls")),
    path(route="api/", view=include(arg="currencies.urls")),
]

urlpatterns += router.urls
