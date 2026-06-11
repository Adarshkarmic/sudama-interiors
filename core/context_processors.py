from services.models import Service


def site_navigation(request):
    return {
        "nav_services": Service.objects.order_by("id"),
        "brand_phone": "+91 87574 77519",
        "brand_email": "enterprisessudama734@gmail.com",
        "brand_location": "MRM college road lalbagh (Darbhanga)",
    }
