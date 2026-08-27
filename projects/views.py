from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from django.db.models import Avg, Count
import resend
from django.contrib import messages
from django.conf import settings
import logging
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required


from .models import Project, Review, ContactMessage
from .forms import ProjectForm, ReviewForm, ContactForm



logger = logging.getLogger(__name__)

def home(request):
    all_projects = Project.objects.all()
    contact_form = ContactForm()

    return render(request, 'project/home.html', {"all_projects":all_projects,  "contact_form": contact_form})



def project_detail(request, pk):

    project = get_object_or_404(Project, pk=pk)

    reviews = project.reviews.filter(approved=True).order_by("-created_at")

    review_form = ReviewForm()


    if request.method == "POST":

        review_form = ReviewForm(request.POST)

        if review_form.is_valid():

            review = review_form.save(commit=False)

            review.project = project

            review.save()

            messages.success(
                request,
                "Your review has been submitted successfully "
                "and is awaiting approval."
            )

            return redirect(
                f"/project/{project.pk}/#reviews"
            )

    # Average rating
    rating_data = reviews.aggregate(
        average_rating=Avg("rating"),
        review_count=Count("id")
    )

    average_rating = rating_data["average_rating"] or 0

    review_count = (
        rating_data["review_count"]
        or 0
    )

    rating_distribution = {}

    for rating in range(5, 0, -1):

        count = reviews.filter(
            rating=rating
        ).count()

        rating_distribution[rating] = count



    return render(request, "project/project_detail.html", {"project": project, "reviews": reviews, "review_form": review_form, "average_rating": average_rating,"review_count": review_count, "rating_distribution": rating_distribution,})

@staff_member_required
def add_project(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('projects:home')
    return render(request, 'project/add_project.html', {"form":form})  


@staff_member_required
def update_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)

        if form.is_valid():
            form.save()
            messages.success(request, "Project updated Successfully")
            return redirect(
                        f"{reverse('projects:home')}#projects"
                    )
        
    context = {
        'form':form,
        'project':project
    }
    return render(request, "project/update_project.html", context)



def services(request):
    return render(request, "project/services.html")


def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"Portfolio Contact from {name}"

        body = f"""
Name: {name}

Email: {email}

Message:

{message}
"""

        try:

            resend.api_key = settings.RESEND_API_KEY

            resend.Emails.send({
                "from": "onboarding@resend.dev",
                "to": [settings.CONTACT_EMAIL],
                "subject": subject,
                "text": body,
                "reply_to": email,
            })

            messages.success(
                request,
                "Your message has been sent successfully."
            )

        except Exception as e:

            print("RESEND EMAIL ERROR:", repr(e))

            messages.error(
                request,
                "Sorry, your message could not be sent "
                "right now. Please try again later."
            )

        return redirect(
            f"{reverse('projects:home')}#contact"
        )

    return redirect(
        f"{reverse('projects:home')}#contact"
    )



@staff_member_required
def delete_project(request, pk):

    project = get_object_or_404(
        Project,
        pk=pk
    )

    if request.method == "POST":

        project_title = project.title

        project.delete()

        messages.success(
            request,
            f'"{project_title}" was deleted successfully.'
        )

        return redirect(
            "projects:home"
        )

    return render(
        request,
        "project/delete_project.html",
        {
            "project": project
        }
    )
