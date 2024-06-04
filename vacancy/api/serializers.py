from rest_framework import serializers
from ..models import Category, Vacancy


class VacancySerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(source='created', format='%d-%m-%Y',
                                     required=False)

    class Meta:
        model = Vacancy
        # exclude = ('created','updated', 'slug')
        fields = ('id', 'category', 'position', 'level', 'salary',
                  'type', 'description', 'number', 'city',
                  'requirements', 'experience', 'offer', 'date', 'status')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        if request and request.resolver_match.url_name == 'category_detail_api':
            vacancies = instance.vacancies.all()
            data['vacancies'] = VacancySerializer(vacancies, many=True).data
        return data
