"""working with model serializers there is no need to  explicity expalin every t field of table 
 will automatically also check validation """

#In model serializers create and update is automatically invoked no need to create its function
from rest_framework import  serializers
from .models import Student

#validators use to validate sepecificc field if that not true it show error 

class StudentSerializers(serializers.ModelSerializer):
    #name=serializers.CharField(read_only=True)
    class Meta:
        model=Student
        fields=['name','roll','city']
        #read_only_fields=['name','roll']
        extra_krwags={'name':{'read_only':True}}

    def validate_roll(self,value):
        if value>200:
            raise serializers.ValidationError("Seat Fulled")
        return value

    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower()=='krishna' and ct.lower()!='mathura':
            raise serializers.ValidationError('city must be mathura')
        return data



"""class StudentSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=100)
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
        return data """




