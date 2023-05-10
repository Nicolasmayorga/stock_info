import uuid
import requests
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import User, APILog
from .serializers import UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        api_key = uuid.uuid4().hex
        serializer.save(api_key=api_key)
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def stock_info(request):
    api_key = request.META.get('HTTP_API_KEY')
    if not api_key:
        return JsonResponse({"detail": "API key required"}, status=status.HTTP_403_FORBIDDEN)

    try:
        user = User.objects.get(api_key=api_key)
    except User.DoesNotExist:
        return JsonResponse({"detail": "Invalid API key"}, status=status.HTTP_403_FORBIDDEN)

    symbol = request.GET.get('symbol')
    if not symbol:
        return JsonResponse({"detail": "Symbol parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    # Llamada a la API de Alpha Vantage
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize=compact&apikey=X86NOH6II01P7R24"
    response = requests.get(url)
    data = response.json()

    if "Error Message" in data:
        return JsonResponse({"detail": "Invalid symbol"}, status=status.HTTP_400_BAD_REQUEST)

    # Procesamiento de la información de la API de Alpha Vantage
    time_series = data.get("Time Series (Daily)", {})
    dates = sorted(time_series.keys(), reverse=True)
    date1, date2 = dates[0], dates[1]
    stock_data1, stock_data2 = time_series[date1], time_series[date2]

    open_price = float(stock_data1["1. open"])
    high_price = float(stock_data1["2. high"])
    low_price = float(stock_data1["3. low"])
    close_price1 = float(stock_data1["4. close"])
    close_price2 = float(stock_data2["4. close"])

    variation = close_price1 - close_price2

    # Registro de la llamada a la API
    APILog.objects.create(user=user, endpoint=request.path)

    return JsonResponse({
        "open": open_price,
        "high": high_price,
        "low": low_price,
        "variation": variation
    }, status=status.HTTP_200_OK)
