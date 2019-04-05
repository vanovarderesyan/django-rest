from django.urls import include, path
from rest_framework import routers
from quickstart import views
from product import views as product_views
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'products', product_views.ItemViewSet)
router.register(r'categories', product_views.CategoriesViewSet)
router.register(r'country', product_views.CountryViewSet)
router.register(r'brands', product_views.BrandsViewSet)
router.register(r'productsimage', product_views.ItemsImageViewSet)
router.register(r'productsvariant', product_views.ItemVariantViewSet)
router.register(r'vender', product_views.DispatcherViewSet)




from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)