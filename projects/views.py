from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Avg, Count
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from django.urls import reverse


from .models import Project, Review, ContactMessage
from .forms import ProjectForm, ReviewForm, ContactForm



def home(request):
    all_projects = Project.objects.all()
    contact_form = ContactForm()

    return render(request, 'project/home.html', {"all_projects":all_projects,  "contact_form": contact_form})

def project_list(request):
    all_projects = Project.objects.all()
    return render(request, 'project/projects.html', {"all_projects":all_projects})

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


def add_project(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('projects:home')
    return render(request, 'project/add_project.html', {"form":form})  

def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            contact_message = form.save()
            email = EmailMessage(

                subject=f"Portfolio Contact: {contact_message.subject}",

                body=f"""
You have received a new message from your portfolio website.

Name:
{contact_message.name}

Email:
{contact_message.email}

Subject:
{contact_message.subject}

Message:
{contact_message.message}
""",

                from_email=settings.DEFAULT_FROM_EMAIL,

                to=[
                    settings.CONTACT_EMAIL
                ],

                reply_to=[
                    contact_message.email
                ],
            )

            email.send(
                fail_silently=False
            )

            messages.success(
                request,
                "Your message has been sent successfully. I'll get back to you soon."
            )

            return redirect(
                f"{reverse('projects:home')}#contact"
            )

    else:
        form = ContactForm()

    return redirect(
        f"{reverse('projects:home')}#contact"
    )
