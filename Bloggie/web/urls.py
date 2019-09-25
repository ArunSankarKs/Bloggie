from django.urls import path, include
from . import views
#your urls will be redirected to their respective function(views) here
urlpatterns = [
    path('article/<id>/',views.article_detail,name='article-detail'),
    path('signup/', views.sign_up , name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('business/', views.business_list,name="business-list"),
    path('business/<id>/', views.business_detail,name="business-detail"),
    path("myprofile",views.myprofile,name="myprofile"),
    path("articles",views.list_article,name="article-list"),
    path("create_article",views.create_article,name="create-article"),
]
