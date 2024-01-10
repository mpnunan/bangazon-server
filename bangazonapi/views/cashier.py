from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import Cashier


class CashierView(ViewSet):
  
    def retrieve(self, request, pk):
        try:
            cashier = Cashier.objects.get(pk=pk)
            serializer = CashierSerializer(cashier)
            return Response(serializer.data)
        except Cashier.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        cashiers = Cashier.objects.all()
        serializer = CashierSerializer(cashiers, many=True)
        return Response(serializer.data)
        
    def create(self, request):
        cashier = Cashier.objects.create(
            uid=request.data["uid"],
            first_name=request.data["firstName"],
            last_name=request.data["lastName"],
            manager=request.data["manager"]
            
        )
        serializer = CashierSerializer(cashier)
        return Response(serializer.data)
    
    def update(self, request, pk):
        cashier = Cashier.objects.get(pk=pk)
        cashier.uid=request.data["uid"]
        cashier.first_name=request.data["firstName"]
        cashier.last_name=request.data["lastName"]
        cashier.manager=request.data["manager"]
        cashier.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        cashier = Cashier.objects.get(pk=pk)
        cashier.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CashierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cashier
        fields = ('id', 'uid', 'first_name', 'last_name', 'manager')
