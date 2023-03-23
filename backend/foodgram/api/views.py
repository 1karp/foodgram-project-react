from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from recipes.models import Recipe, Tag, Ingredient
from users.models import User

from .pagination import PageLimitPagination
from .serializers import RecipeSerializer, TagSerializer, IngredientSerializer, UserSerializer


class TagViewSet(ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = PageLimitPagination


class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
