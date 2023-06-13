from rest_framework import serializers
from .models import Customer
from .models import OrderPlaced
from .models import Cart
from .models import Product
from .models import Feedback

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class OrderPlacedSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPlaced
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"
