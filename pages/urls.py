from .views import HomePageView, PasswordPageView, PostPageView, ProfilePageView
from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name = 'article-list'),
    path('new-post/', PostPageView.as_view(), name = 'article_name'),
    path('profile/', ProfilePageView.as_view(), name = 'interface'),
]