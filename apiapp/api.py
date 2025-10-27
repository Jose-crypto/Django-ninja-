from ninja import Router
from django.urls import path

router=Router()

@router.get('/home', description='Initial route of the API')
def home(request):
    return {'A lannister always pays their debts'}



@router.get('/rock/{int:height}', description='get height of the Casterly Rock')
def height(request, height: int):
    return f'Casterly Rock is: {height+1}m tall' 