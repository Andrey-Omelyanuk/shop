# -*- coding: utf-8 -*-
from rest_framework.viewsets import ModelViewSet
from .serializers import * 


class SmartPhoneViewSet(ModelViewSet):
	queryset         = Smartphone.objects.all()
	serializer_class = SmartphoneSerializer
