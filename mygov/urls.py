from django.urls import path, include
from .views import ParentsViewSet, ChildrenViewSet, WorkHistoryViewSet, EducationsViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework import routers
router = routers.DefaultRouter()
router.register('parents', ParentsViewSet)
router.register('children', ChildrenViewSet)
router.register('workhistory', WorkHistoryViewSet)
router.register('educations', EducationsViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
