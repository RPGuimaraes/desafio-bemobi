from django.urls import path

from tiny.views import *


urlpatterns = [

    path('create', create, name="create-url"),
    path('show-ranking', ranking, name="ranking-url"),
    path('<slug:alias>', RetrieveView.as_view(), name="retrive-url"),



]
