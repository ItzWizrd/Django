from .serilizers import OrderSerializer
from rest_framework import GenericAPIView,status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from Orders.models import Order

class OrderListCreateAPIView(GenericAPIView):
    serializer_class = OrderSerializer

    def get(self, request):
        data = Order.objects.all()
        serializer = self.serializer_class(data, many=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)