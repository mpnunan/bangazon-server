from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import Item

class ItemView(ViewSet):
  
    def retrieve(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
            serializer = ItemSerializer(item)
            return Response(serializer.data)
        except Item.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
        
    def create(self, request):
        item = Item.objects.create(
            name=request.data["name"],
            description=request.data["description"],
            price=request.data["price"]
            
        )
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    
    def update(self, request, pk):
        item = Item.objects.get(pk=pk)
        item.name=request.data["name"]
        item.description=request.data["description"]
        item.price=request.data["price"]
        item.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'price')
