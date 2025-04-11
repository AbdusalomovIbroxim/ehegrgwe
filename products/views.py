from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Project, Category, SubCategory
from .serializers import ProductSerializer, ProjectSerializer, CategorySerializer, SubCategorySerializer


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
        project = Project.objects.last()
        if not project:
            return Response({"detail": "No project found"}, status=404)

        time_remaining = project.get_time_remaining()

        project_data = ProjectSerializer(project).data

        return Response({
            "project": project_data,
            "time_remaining": time_remaining
        })


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_context(self):
        return {'request': self.request}


class SubCategoryListView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_context(self):
        return {'request': self.request}
