from django.db import models


# -----------------------
# HERO SECTION
# -----------------------

class SEOMeta(models.Model):
    """Store SEO metadata for pages"""
    page_name = models.CharField(max_length=100, unique=True)
    meta_title = models.CharField(max_length=60, help_text="60 chars max")
    meta_description = models.CharField(max_length=160, help_text="160 chars max")
    meta_keywords = models.CharField(max_length=200, blank=True)
    og_image = models.ImageField(upload_to="seo/", blank=True)
    canonical_url = models.URLField(blank=True)

    def __str__(self):
        return self.page_name

    class Meta:
        verbose_name_plural = "SEO Meta Tags"

class HeroSection(models.Model):
    logo = models.ImageField(upload_to="hero/")
    title = models.CharField(max_length=255)
    subtitle_1 = models.CharField(max_length=500)
    subtitle_2 = models.CharField(max_length=500)
    button_text = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# -----------------------
# CONSULTING SERVICES (مجالات الإستشارة)
# -----------------------
class ServiceCategory(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to="services/")

    def __str__(self):
        return self.name


# -----------------------
# CORE SERVICES (الخدمات الرئيسية)
# -----------------------
class CoreService(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class CoreServiceItem(models.Model):
    core_service = models.ForeignKey(CoreService, related_name="items", on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text[:40]



# -----------------------
# CONTACT INFO
# -----------------------
class ContactMethod(models.Model):
    CONTACT_TYPES = [
        ("phone", "Phone"),
        ("email", "Email"),
        ("whatsapp", "WhatsApp"),
    ]

    type = models.CharField(max_length=20, choices=CONTACT_TYPES)
    icon = models.CharField(max_length=10, help_text="Emoji or icon text")
    value = models.CharField(max_length=255)
    button_text = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.value


# -----------------------
# FOOTER
# -----------------------


class FooterContact(models.Model):
    text = models.CharField(max_length=200)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class SocialLink(models.Model):
    platform = models.CharField(max_length=50)  # f, in, ig
    url = models.URLField()

    def __str__(self):
        return self.platform


class FooterInfo(models.Model):
    copyright_text = models.CharField(max_length=255)

    def __str__(self):
        return "Footer Info"
