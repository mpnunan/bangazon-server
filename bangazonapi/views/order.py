from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import Order, Cashier, Customer


class OrderView(ViewSet):
  
    def retrieve(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        orders = Order.objects.all()
        
        is_open = request.query_params.get('is_open', None)
        if is_open is not None:
            orders = orders.filter(is_open=is_open)
        
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
        
    def create(self, request):
        cashier = Cashier.objects.get(uid=request.data["uid"])
        customer = Customer.objects.get(pk=request.data["customerId"])
        order = Order.objects.create(
            cashier=cashier,
            customer=customer,
            open_time=request.data["openTime"],
            close_time=request.data["closeTime"],
            is_open=request.data["isOpen"],
            type=request.data["type"],
            payment_type=request.data["paymentType"],
            tip_amount=request.data["tipAmount"],
            total=request.data["total"]
        )
        serializer = OrderSerializerShallow(order)
        return Response(serializer.data)

    def update(self, request, pk):
        cashier = Cashier.objects.get(uid=request.data["uid"])
        customer = Customer.objects.get(pk=request.data["customerId"])
        order = Order.objects.get(pk=pk)
        order.cashier=cashier
        order.customer=customer
        order.open_time=request.data["openTime"]
        order.close_time=request.data["closeTime"]
        order.is_open=request.data["isOpen"]
        order.type=request.data["type"]
        order.payment_type=request.data["paymentType"]
        order.tip_amount=request.data["tipAmount"]
        order.total=request.data["total"]
        order.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'cashier', 'customer', 'open_time', 'close_time', 'is_open', 'type', 'payment_type', 'tip_amount', 'total')
        depth = 1

class OrderSerializerShallow(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'cashier_id', 'customer_id', 'open_time', 'close_time', 'is_open', 'type', 'payment_type', 'tip_amount', 'total')
