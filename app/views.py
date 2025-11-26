# ...existing code...
from django.shortcuts import render
import datetime
from .models import (
    SEOMeta, HeroSection, ServiceCategory, CoreService,
    ContactMethod, FooterContact, SocialLink, FooterInfo
)



def home_view(request):

    seo = SEOMeta.objects.filter(page_name="home").first()

    hero = HeroSection.objects.first()
    services = ServiceCategory.objects.all()
    core_services = CoreService.objects.prefetch_related("items").all()
    contact_methods = ContactMethod.objects.all()
    footer_contact = FooterContact.objects.all()
    social_links = SocialLink.objects.all()
    footer_info = FooterInfo.objects.first()

    context = {
        "seo": seo,
        "hero": hero,
        "services": services,
        "core_services": core_services,
        "contact_methods": contact_methods,
        "footer_contact": footer_contact,
        "social_links": social_links,
        "footer_info": footer_info,
        "current_year": datetime.date.today().year,
    }

    return render(request, "index.html", context)
