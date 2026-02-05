from django_distill import distill_path
from . import views

def empty():
    return None

urlpatterns = [
    distill_path("", views.home, name="home"),
    distill_path("home/", views.home, name="home_redirect", distill_func=empty),

    distill_path("about/", views.about, name="about"),
    distill_path("project/", views.project, name="project"),
    distill_path("education/", views.education, name="education"),
    distill_path("cv/", views.cv, name="cv"),
    distill_path("contact/", views.contact, name="contact"),
]