from rest_framework import serializers
from .models import *


class AcctcustSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Acctcust
        # fields = '__all__'
        fields = (
            'id', 'acctname', 'businesssec', 'regulatory',
        )
