from api.models import SensorNode
from rest_framework import serializers

class UnixEpochDateField(serializers.DateTimeField):
    def to_native(self, value):
        import time
        try:
            return int(time.mktime(value.timetuple()))
        except (AttributeError, TypeError):
            return None
    def from_native(self, value):
        import datetime
        return datetime.datetime.fromtimestamp(int(value))

class SensorNodeSerializer(serializers.HyperlinkedModelSerializer):
    created = UnixEpochDateField(source='created')
    class Meta:
        model = SensorNode
        fields = ('id', 'code', 'name', 'description', 'created')
