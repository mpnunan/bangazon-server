from bangazonapi.models import Cashier
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def check_user(request):
    uid = request.data['uid']
    cashier = Cashier.objects.filter(uid=uid).first()

    if cashier is not None:
        data = {
            'id': cashier.id,
            'uid': cashier.uid,
            'first_name': cashier.first_name,
            'last_name': cashier.last_name,
            'manger': cashier.manager
        }
        return Response(data)
    else:
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    cashier = Cashier.objects.create(
        uid=request.data['uid'],
        first_name=request.data['firstName'],
        last_name=request.data['lastName'],
        manager=request.data['manager']
    )

    data = {
        'id': cashier.id,
        'uid': cashier.uid,
        'first_name': cashier.first_name,
        'last_name': cashier.last_name,
        'manager': cashier.manager
    }
    return Response(data)
