"""TPW_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf import settings
from app import views
from app.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    # path('', include('django_app.urls')),

    path('login/', auth_views.LoginView.as_view(template_name="index.html", authentication_form=LoginForm), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    path('signup/', views.signup, name='signup'),

    path('articles/', views.articles, name='articles'),
    path('articles/<str:article_type>/', views.articles, name='articles_type'),
    path('articles/games/<str:article_platform>/', views.articles, name='articles_platform'),

    path('article/<int:article_id>/', views.article_details, name='article_details'),

    path('new/article/', views.create_article1, name='create_article1'),
    path('new/article2/', views.create_article2, name='create_article2'),
    path('update/article/<int:article_id>/', views.edit_article, name='edit_article'),

    path('new/article/game/', views.create_game, name='create_game'),
    path('update/article/game/<int:game_id>/', views.edit_game, name='edit_game'),

    path('shopcart/', views.shop_cart, name='shop_cart'),

    path('owned/articles/<int:user_id>', views.articles_owned, name='articles_owned'),
    path('saved/articles/', views.articles_saved, name='articles_saved'),

    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('update/profile/', views.edit_profile, name='edit_profile'),

    path('settings/', views.settings, name='settings')

]

# Serving the media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
