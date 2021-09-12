from django.contrib.auth.models import User, Group
from rest_framework import generics, mixins, permissions, viewsets

from quickstart.models import Order
from quickstart.serializers import UserSerializer, GroupSerializer, OrderSerializer
from quickstart.tasks import cook_pizza, bill

from utils import send_email


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.GenericViewSet,
                   mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        customer = request.data.get('customer')
        email = request.data.get('email')

        cook_pizza.apply_async((email, customer), countdown=5)
        bill.apply_async((email, customer), countdown=5)

        return super().create(request, *args, **kwargs)
