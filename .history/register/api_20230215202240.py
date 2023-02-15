from ninja import NinjaAPI, ModelSchema
from .models import Composition
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

api = NinjaAPI()

@api.get('composition/')
def list(request):
    composition = Composition.objects.all()
    response = [{'id': i.id, 'title': i.title, 'lyrics': i.lyrics, 'composer': i.composer } for i in composition]
    return response

@api.get('composition/{title}')
def search_by_title(request, title : str):
    composition = get_object_or_404(Composition, title=title)
    return model_to_dict(composition)

class CompositionSchema(ModelSchema):
    class Config:
        model = Composition
        model_fields = "__all__"
        
@api.post ('composition', response=CompositionSchema)
def create_composition(request, composition: CompositionSchema):
    c1 = composition.dict()
    composition = Composition(**c1)
    composition.save()
    return composition