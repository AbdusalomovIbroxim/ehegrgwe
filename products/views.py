from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Project
from .serializers import ProductSerializer, ProjectSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all().select_related('category', 'subcategory')
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_context(self):
        return {'request': self.request}


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_context(self):
        return {'request': self.request}


class ToggleFavoriteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        if request.user in product.favorites.all():
            product.favorites.remove(request.user)
            return Response({'status': 'removed from favorites'})
        else:
            product.favorites.add(request.user)
            return Response({'status': 'added to favorites'})


class TimeReportView(APIView):
    def get(self, request):
        # Получаем последний проект
        project = Project.objects.last()  # Возвращает последний объект проекта
        if not project:
            return Response({"detail": "No project found"}, status=404)

        # Получаем время до конца (если проект еще не завершен)
        time_remaining = project.get_time_remaining()  # Время, которое осталось

        # Сериализуем объект проекта
        project_data = ProjectSerializer(project).data

        # Возвращаем данные проекта и время до окончания
        return Response({
            "project": project_data,
            "time_remaining": time_remaining
        })

