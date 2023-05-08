from django.contrib import admin

from django.urls import path, include, re_path
from auction.views import ActiveLotsAPIList, LotAPIUpdate, LotAPIDestroy, NewBetInLotUpdate, BuyersLotsAPIList, csrf
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/lots/', ActiveLotsAPIList.as_view()),
    path('api/lot/<int:pk>/', LotAPIUpdate.as_view()),
    path('api/delete-lot/<int:pk>/', LotAPIDestroy.as_view()),
    path('api/lot/<int:pk>/bet/', NewBetInLotUpdate.as_view()),
    path('api/buyerslots/', BuyersLotsAPIList.as_view()),

    path('api/register/', include('djoser.urls')),

    path('api/csrf/', csrf),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
