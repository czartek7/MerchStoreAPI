from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'price',
            'stock',
            'description',
            'product_img'
        )
        model = Product