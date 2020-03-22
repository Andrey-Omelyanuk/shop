# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from ..models import *


class SmartphoneSerializer(ModelSerializer):
	class Meta:
		model = Smartphone
		fields = '__all__'


