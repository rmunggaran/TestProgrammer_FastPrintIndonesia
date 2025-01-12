from rest_framework import serializers
from .models import Produk, Kategori, Status

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = '__all__'
