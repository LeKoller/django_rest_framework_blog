from django.urls import path
from .views import Home, Article


urlpatterns = [
    path('', Home.as_view()),
    path('articles', Article.as_view())
]
