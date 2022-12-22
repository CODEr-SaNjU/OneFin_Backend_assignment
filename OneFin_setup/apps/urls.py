from django.urls import path
from .views import func


# router.register(r'api/v1/dao/category', DaoCategoryView, basename="dao_category")
# router.register(r'api/v1/dao/review', UserReviewRatingViewSet, basename="dao_rating")

urlpatterns = [
     path('', func, name='home'),
]