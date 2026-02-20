from django.urls import path
from .views import RelationDBView

urlpatterns = [
    path('people/', RelationDBView.as_view(), name='relation_db'),
]