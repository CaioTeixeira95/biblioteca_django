from .models import Books, Loan, User
from .serializers import BooksSerializer, LoanSerializer, UserSerializer
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_condition import Or
from oauth2_provider.contrib.rest_framework import (
    TokenHasReadWriteScope,
    OAuth2Authentication
)

"""

O atributo 'authentication_classes' define quais tipos de autenticação a view
vai aceitar, o OAuth2Authentication refere-se a autenticação
padrão OAuth2 e SessionAuthentication é o padrão de autenticação utilizado
pelo admin do Django.

O atributo 'permission_classes' define quais
as permissões necessárias para se ter acesso a view.

O atributo 'filter_backends' define o filtro padrão da view,
no caso o DjangoFilterBackend está sendo colocado como o
filtro padrão.

O atributo 'filter_fields' indica quais campos podem ser passados como filtros,
nesse caso todos os campos poderão ser usados como filtro.

"""


class BooksList(generics.ListCreateAPIView):

    queryset = Books.objects.all()
    serializer_class = BooksSerializer

    """
        Definindo que apenas usuários autenticados poderão visualizar.
        Caso o usuário não esteja autenticado retornará uma mensagem
        dizendo que as informações de autenticação não foram fornecidas
    """
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAuthenticated, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = '__all__'


class BooksDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [Or(IsAuthenticated, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = '__all__'


class LoanList(generics.ListCreateAPIView):

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [Or(IsAuthenticated, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = '__all__'


class LoanDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [Or(IsAuthenticated, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = '__all__'


class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [Or(IsAuthenticated, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = '__all__'


class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [Or(IsAuthenticated, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = '__all__'
