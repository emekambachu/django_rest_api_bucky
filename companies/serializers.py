from rest_framework import serializers
from . models import Stock


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock

        # return specific fields
        # fields = ('ticker', 'volume')

        # return all fields
        fields = '__all__'
