from django.http import JsonResponse
from .models import Hotel


def hotels_list(request):
    """Получение отелей по API"""

    # Получение path-параметров
    city_id = request.GET.get('city_id')
    from_id = request.GET.get('from_id')
    limit = request.GET.get('limit')

    # Валидация параметров
    if city_id is not None and not city_id.isdigit():
        return JsonResponse({'error': 'city_id должен быть числом'}, status=400)
    if from_id is not None and not from_id.isdigit():
        return JsonResponse({'error': 'from_id должен быть числом'}, status=400)
    if limit is not None and not limit.isdigit():
        return JsonResponse({'error': 'limit должен быть числом'}, status=400)

    # Запрос queryset
    queryset = Hotel.objects.all()

    # Фильтрация queryset
    if city_id:
        queryset = queryset.filter(city_id=city_id)
    if from_id:
        queryset = queryset.filter(id__gt=from_id)
    if limit:
        queryset = queryset[:int(limit)]

    output_result = list(queryset.values())

    status = 200
    if not output_result:
        status = 204

    return JsonResponse(output_result, safe=False, status=status)
