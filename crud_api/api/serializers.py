from rest_framework import  serializers
from .models import Student

#validators use to validate sepecificc field if that not true it show error 

def start_with_r(value):
    if value[0].lower() !='a':
        raise serializers.ValidationError("Name must start with A")




class StudentSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=100,  validators=[start_with_r])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance

    #Field level validation for singal field

    def validate_roll(self,value):
        if value>200:
            raise serializers.ValidationError("Seat Fulled")
        return value

    # Object level validation for multiple fields

    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower()=='krishna' and ct.lower()!='mathura':
            raise serializers.ValidationError('city must be mathura')
        return data 




