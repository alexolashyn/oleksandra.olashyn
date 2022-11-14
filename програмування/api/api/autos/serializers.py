from rest_framework import serializers
from .models import Auto
from .validation import Validation


class AutoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    brand = serializers.CharField(max_length=200, required=True)
    model = serializers.CharField(max_length=200, required=True)
    registration_number = serializers.CharField(max_length=8, required=True)
    bought_at = serializers.CharField(max_length=10, required=True)
    repaired_at = serializers.CharField(max_length=10, required=True)
    car_mileage = serializers.IntegerField(required=True)

    def validate(self, data):
        errors_dict = {}
        Validation.numeric_validation(data['id'], errors_dict)
        Validation.brand_validation(data['brand'], errors_dict)
        Validation.model_validation(data['model'], errors_dict)
        Validation.registration_number_validation(data['registration_number'], errors_dict)
        Validation.date_validation(data['bought_at'], errors_dict)
        Validation.date_validation(data['repaired_at'], errors_dict)
        Validation.inappropriate_date(data['bought_at'], data['repaired_at'], errors_dict)
        Validation.numeric_validation(data['car_mileage'], errors_dict)
        if len(errors_dict):
            raise serializers.ValidationError(errors_dict)
        return data

    class Meta:
        model = Auto
        fields = ('__all__')


