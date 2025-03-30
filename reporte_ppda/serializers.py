# from rest_framework import serializers
# from .models import Organismo, MedidaPPDA, AvanceMedida

# class OrganismoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Organismo
#         fields = '__all__'

# class MedidaPPDASerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MedidaPPDA
#         fields = '__all__'

# class AvanceMedidaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AvanceMedida
#         fields = '__all__'


from rest_framework import serializers
from .models import Organismo, MedidaPPDA, AvanceMedida

class OrganismoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organismo
        fields = '__all__'

class MedidaPPDASerializer(serializers.ModelSerializer):
    class Meta:
        model = MedidaPPDA
        fields = '__all__'

class AvanceMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvanceMedida
        fields = '__all__'
