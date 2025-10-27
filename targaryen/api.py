from django.shortcuts import get_object_or_404
from targaryen.models import Person
from ninja import Router
from targaryen.schemas import DragonOut

router = Router()


@router.get('/dragons', response=list[DragonOut], description='GET Dragons lists')
def dragons(request):
    data = [
        DragonOut(name='Drogon',birth_year=1993),
        DragonOut(name='Rheal',birth_year=2000),
    ]
    return data