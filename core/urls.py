from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books/$', views.BooksList.as_view(), name='books-list'),
    url(
        r'^books/(?P<pk>[0-9]+)/$',
        views.BooksDetail.as_view(),
        name='books-detail'
    ),

    url(r'^loan/$', views.LoanList.as_view(), name='loan-list'),
    url(
        r'^loan/(?P<pk>[0-9]+)/$',
        views.LoanDetail.as_view(),
        name='loan-detail'
    ),

    url(r'^user/$', views.UserList.as_view(), name='user-list'),
    url(
        r'^user/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail'
    ),
]
