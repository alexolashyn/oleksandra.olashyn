from .views import AutoView
from django.urls import path

urlpatterns = [
    path('basic/', AutoView.as_view()),
    path('basic/<int:id>/', AutoView.as_view()),
    path('basic/<int:id>/update/', AutoView.as_view())
]