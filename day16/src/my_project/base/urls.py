from django.urls import path
from .views import ListaPendientes, DetalleTarea,CrearTarea

urlpatterns = [
    path("",ListaPendientes.as_view(),name="tareas"),
    path("tarea/<int:pk>/",DetalleTarea.as_view(),name="tarea"),
    path("crear-tarea/",CrearTarea.as_view(),name="crear-tarea"),
]