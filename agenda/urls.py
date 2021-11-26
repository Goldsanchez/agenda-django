from django.urls import path
from .views import AgendaListView, AgendaCreateView, AgendaUpdateView, AgendaDeleteView

urlpatterns = [
    path('', AgendaListView.as_view(), name='home'),
    path('create/', AgendaCreateView.as_view(), name="create"),
    path('update/<int:pk>', AgendaUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', AgendaDeleteView.as_view(), name="delete"),
]