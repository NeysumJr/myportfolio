from django.contrib import admin
from .models import About, Project,OwnerContactInfo, VisitorMessage, SiteImage, Education, Skill, Stat, Testimonial, CV
# Register your models here.
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Stat)
admin.site.register(Testimonial)
admin.site.register(Project)
admin.site.register(OwnerContactInfo)
admin.site.register(VisitorMessage)
admin.site.register(SiteImage)
admin.site.register(Education)
admin.site.register(CV)