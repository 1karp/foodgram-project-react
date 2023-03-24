from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import IngredientViewSet, RecipeViewSet, TagViewSet, UserViewSet

router_v1 = DefaultRouter()

router_v1.register(
    'recipes',
    RecipeViewSet,
    basename='recipes'
)
router_v1.register(
    'tags',
    TagViewSet,
    basename='tags'
)
router_v1.register(
    'ingredients',
    IngredientViewSet,
    basename='ingredients'
)
router_v1.register(
    'users',
    UserViewSet,
    basename='users'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    # path('v1/auth/signup/', register, name='register'),
    # path('v1/auth/token/', get_token, name='token'),
]
