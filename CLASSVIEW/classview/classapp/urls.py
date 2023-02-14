from django.urls import include, re_path

from django.contrib import admin

from classapp import views


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^welcome', views.WelcomeView.as_view()),
    re_path(r'^my-books/',views.BooksView.as_view()),
    re_path(r'^book-detail-by-id/(?P<pk>[-\w]+)',views.BookDetailByIdView.as_view()),
    re_path(r'^book-detail-by-code/(?P<code>[-\w]+)',
        views.BookDetailByCodeView.as_view()),
    re_path(r'^book-update/(?P<pk>[-\w]+)$', views.BookUpdateView.as_view()),
    re_path(r'^book-create$', views.BookCreateView.as_view()),
    re_path(r'^author-create$', views.AuthorCreateView.as_view()),

]