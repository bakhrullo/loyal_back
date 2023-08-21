from django.db import transaction
from django.db.models import F
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from loyal_app.models import *
from loyal_app.serializers import *


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    lookup_field = 'tg_id'
    queryset = User.objects.all()


class UserGetView(RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'tg_id'
    queryset = User.objects.all()


class BonusView(APIView):

    @transaction.atomic
    def update_balance(self, tg_id: int, bonus_point: int, bonus: Bonus):
        user = User.objects.get(tg_id=tg_id)
        user.point += bonus_point
        user.save()
        bonus.user = user
        bonus.save()

    def get(self, request):
        try:
            bonus = Bonus.objects.get(code=request.query_params.get("code"))
            if bonus.user is None:
                self.update_balance(tg_id=request.query_params.get("tg_id"), bonus_point=bonus.point, bonus=bonus)
                return Response(status=status.HTTP_200_OK, data={"status": "OK"})
            return Response(status=status.HTTP_200_OK, data={"status": "In use"})
        except Bonus.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"status": "Not found"})


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductGetView(RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class NewsListView(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class NewsGetView(RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = NewsSerializer
    queryset = Product.objects.all()
