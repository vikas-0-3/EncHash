from django.urls import path, include
from enchash import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('textencryption', views.textencryption, name="textencryption"),
    path('imageencryption', views.imageencryption, name="imageencryption"),

    path('selfalgo', views.selfalgo, name="selfalgo"),
    path('selfalgodec', views.selfalgo2, name="selfalgodec"),
    path('clubalgo', views.clubalgo, name="clubalgo"),
    path('clubbingalgos', views.clubbingalgos, name="clubbingalgos"),
    path('clubbingalgosdec', views.clubbingalgosdec, name="clubbingalgosdec"),

    path('imageenc', views.imageenc, name="imageenc"),

]



# uncomment for media files : 
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#     document_root=settings.MEDIA_ROOT)


    