from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('affiliate/', views.affiliate, name='affiliate'),
    path('articles/', views.articles, name='articles'),
    path('blog/', views.blog, name='blog'),
    path('contacts/', views.contacts, name='contacts'),
    path('contest/', views.contest, name='contest'),
    path('faq/', views.faq, name='faq'),
    path('forgot/', views.forgot, name='forgot'),
    path('how/', views.how, name='how'),
    path('index-2/', views.index_2, name='index-2'),
    path('index2/', views.index2, name='index2'),
    path('invest/', views.invest, name='invest'),
    path('privacy/', views.privacy, name='privacy'),
    path('profile/', views.profile, name='profile'),
    path('reports/', views.reports, name='reports'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('token/', views.token, name='token'),
    path('custom-404/', views.custom_404, name='custom-404'),
]

handler404 = 'bitcoin.views.custom_404'
