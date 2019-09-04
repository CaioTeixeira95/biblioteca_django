from rest_framework import serializers
from .models import Books, Loan, User


class BooksSerializer(serializers.ModelSerializer):

    class Meta:

        model = Books
        fields = '__all__'


class LoanSerializer(serializers.ModelSerializer):

    class Meta:

        model = Loan
        fields = '__all__'

    def create(self, validated_data):

        loan, created = Loan.objects.get_or_create(
            id_book=validated_data.get('id_book'),
            is_devolved=False,
            defaults=validated_data
        )

        return loan


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = '__all__'
