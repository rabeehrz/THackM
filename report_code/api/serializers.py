from rest_framework import serializers
from report_code.models import ReportCode

class ReportCodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = ReportCode
		fields = '__all__'