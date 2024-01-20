from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import OrderItem


class OrderItemView(ViewSet):
  
    def retrieve(self, request, pk):
        try:
            order_item = OrderItem.objects.get(pk=pk)
            serializer = OrderItemSerializer(order_item)
            return Response(serializer.data)
        except OrderItem.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        order_items = OrderItem.objects.all()
        serializer = OrderItemSerializer(order_items, many=True)
        return Response(serializer.data)
        
    def create(self, request):
        order_item = OrderItem.objects.create(
            order=request.data["order"],
            item=request.data["item"],
        )
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data)
    
    def update(self, request, pk):
        order_item = OrderItem.objects.get(pk=pk)
        order_item.order=request.data["order"]
        order_item.item=request.data["item"]
        order_item.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        item = OrderItem.objects.get(pk=pk)
        item.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ('id', 'order_id', 'item')
        depth = 1
