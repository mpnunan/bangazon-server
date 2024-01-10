from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import Customer


class CustomerView(ViewSet):
  
    def retrieve(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        except Customer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
        
    def create(self, request):
        customer = Customer.objects.create(
            name=request.data["name"],
            email=request.data["email"],
            phone_number=request.data["phoneNumber"]
        )
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def update(self, request, pk):
        customer = Customer.objects.get(pk=pk)
        customer.name=request.data["name"]
        customer.email=request.data["email"]
        customer.phone_number=request.data["phoneNumber"]
        customer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        customer = Customer.objects.get(pk=pk)
        customer.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('id', 'name', 'email', 'phone_number')
