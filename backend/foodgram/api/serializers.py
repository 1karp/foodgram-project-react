from recipes.models import Ingredient, Recipe, Tag, Favorites, Cart
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from users.models import Follow, User


class ShortRecipeSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = 'id', 'name', 'image', 'cooking_time'
        read_only_fields = '__all__',


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
        read_only_fields = '__all__',


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = '__all__',


class UserSerializer(ModelSerializer):
    is_subscribed = SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed',
            'password',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def get_is_subscribed(self, user):
        request = self.context.get('request')
        if request is None or request.user.is_anonymous:
            return False
        return Follow.objects.filter(user=request.user, author=user).exists()

    def create(self, validated_data: dict) -> User:
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class RecipeSerializer(ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    author = UserSerializer(read_only=True)
    is_favorited = SerializerMethodField()
    is_in_shopping_cart = SerializerMethodField()

    class Meta:
        model = Recipe
        fields = (
            'id',
            'tags',
            'author',
            'ingredients',
            'is_favorited',
            'is_in_shopping_cart',
            'name',
            'image',
            'text',
            'cooking_time',
        )

    def get_is_favorited(self, recipe):
        user = self.context.get('request').user
        return user.is_authenticated and Favorites.objects.filter(
            user=user, recipe=recipe.id
        ).exists()

    def get_is_in_shopping_cart(self, recipe):
        user = self.context.get('request').user
        return user.is_authenticated and Cart.objects.filter(
            user=user, recipe=recipe.id
        ).exists()


class UserFollowSerializer(UserSerializer):
    recipes = ShortRecipeSerializer(many=True, read_only=True)
    recipes_count = SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed',
            'recipes',
            'recipes_count',
        )
        read_only_fields = '__all__',

    def get_recipes_count(self, user):
        return user.recipes.count()


# class TokenSerializer(Serializer):
#     email = CharField(
#         label='Email',
#         write_only=True)
#     password = CharField(
#         label='Пароль',
#         style={'input_type': 'password'},
#         trim_whitespace=False,
#         write_only=True)
#     token = CharField(
#         label='Токен',
#         read_only=True)

#     def validate(self, attrs):
#         email = attrs.get('email')
#         password = attrs.get('password')
#         if email and password:
#             user = authenticate(
#                 request=self.context.get('request'),
#                 email=email,
#                 password=password)
#             if not user:
#                 raise ValidationError(
#                     ERR_MSG,
#                     code='authorization')
#         else:
#             msg = 'Необходимо указать "адрес электронной почты" и "пароль".'
#             raise ValidationError(
#                 msg,
#                 code='authorization')
#         attrs['user'] = user
#         return attrs
