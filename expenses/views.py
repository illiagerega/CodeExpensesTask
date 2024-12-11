from rest_framework import viewsets, generics
from rest_framework.response import Response
from django.db.models import Sum
from .models import User, Expense
from .serializers import UserSerializer, ExpenseSerializer
from rest_framework.decorators import action
from datetime import datetime

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    @action(detail=False, methods=['get'], url_path='by-date-range')
    def list_by_date_range(self, request):
        user_id = request.query_params.get('user_id')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if not all([user_id, start_date, end_date]):
            return Response({"error": "user_id, start_date, and end_date are required."}, status=400)

        expenses = Expense.objects.filter(
            user_id=user_id,
            date__range=[start_date, end_date]
        )
        serializer = self.get_serializer(expenses, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='category-summary')
    def category_summary(self, request):
        user_id = request.query_params.get('user_id')
        month = request.query_params.get('month')

        if not all([user_id, month]):
            return Response({"error": "user_id and month are required."}, status=400)

        month_date = datetime.strptime(month, '%Y-%m')
        expenses = Expense.objects.filter(
            user_id=user_id,
            date__year=month_date.year,
            date__month=month_date.month
        )
        summary = expenses.values('category').annotate(total=Sum('amount'))
        return Response(summary)