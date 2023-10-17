from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from tareas import views


#versionado de API
router = routers.DefaultRouter()
router.register(r'tareas', views.VistaTareas, 'tareas')

#forma de definir las rutas
urlpatterns = [
    path('api/', include(router.urls)) ,
    path('docs/', include_docs_urls(title="Tareas API"))
]

# Esto generada las peticiones GET, POST, PUT, DELETE