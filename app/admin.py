from django.contrib import admin
from .models import (
    SEOMeta, HeroSection, ServiceCategory, CoreService, CoreServiceItem,
    ContactMethod, FooterContact, SocialLink, FooterInfo
)
admin.site.site_header = "Kemét Consulting Admin"
admin.site.site_title = "Kemét Admin"
admin.site.index_title = "Site Management"

@admin.register(SEOMeta)
class SEOMetaAdmin(admin.ModelAdmin):
    list_display = ("page_name", "meta_title")
    search_fields = ("page_name", "meta_title", "meta_description")
    list_filter = ("page_name",)
    fieldsets = (
        ("Page Information", {
            "fields": ("page_name",)
        }),
        ("Meta Tags", {
            "fields": ("meta_title", "meta_description", "meta_keywords")
        }),
        ("Open Graph", {
            "fields": ("og_image", "canonical_url")
        }),
    )

class CoreServiceItemInline(admin.TabularInline):
    model = CoreServiceItem
    extra = 1

@admin.register(CoreService)
class CoreServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    inlines = [CoreServiceItemInline]
    ordering = ("title",)

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "button_text")
    search_fields = ("title",)

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(ContactMethod)
class ContactMethodAdmin(admin.ModelAdmin):
    list_display = ("value", "type", "icon", "button_text")
    list_filter = ("type",)
    search_fields = ("value",)

@admin.register(FooterContact)
class FooterContactAdmin(admin.ModelAdmin):
    list_display = ("text", "link")
    search_fields = ("text",)

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("platform", "url")
    search_fields = ("platform",)

@admin.register(FooterInfo)
class FooterInfoAdmin(admin.ModelAdmin):
    list_display = ("copyright_text",)