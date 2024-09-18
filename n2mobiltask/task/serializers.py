from rest_framework import serializers
from .models import Address, Geo, Company, Users, Albums, Photos, Posts, Comments, Todos

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    geo = GeoSerializer()
    company = CompanySerializer()

    class Meta:
        model = Users
        fields = '__all__'

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        geo_data = validated_data.pop('geo')
        company_data = validated_data.pop('company')

        # Create Address instance
        address = Address.objects.create(**address_data)

        # Create Geo instance
        geo = Geo.objects.create(**geo_data)

        # Create Company instance
        company = Company.objects.create(**company_data)

        # Create User instance
        user = Users.objects.create(address=address, geo=geo, company=company, **validated_data)

        return user


    def update(self, instance, validated_data):

        address_data = validated_data.pop('address', None)
        geo_data = validated_data.pop('geo', None)
        company_data = validated_data.pop('company', None)

        instance.name = validated_data.get('name', instance.name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.website = validated_data.get('website', instance.website)
        instance.save()

        if address_data:
            Address.objects.filter(pk=instance.address.pk).update(**address_data)

        if geo_data:
            Geo.objects.filter(pk=instance.geo.pk).update(**geo_data)

        if company_data:
            Company.objects.filter(pk=instance.company.pk).update(**company_data)

        return instance

class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = '__all__'

class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = '__all__'

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = '__all__'
