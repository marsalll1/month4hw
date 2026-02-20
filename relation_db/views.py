from django.views.generic import ListView
from .models import Register

class RelationDBView(ListView):
    model = Register
    template_name = 'relation_db.html'
    context_object_name = 'tours'