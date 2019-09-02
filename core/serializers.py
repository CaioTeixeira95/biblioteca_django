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


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = '__all__'
