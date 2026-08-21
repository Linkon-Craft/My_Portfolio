from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):

    class Meta:

        model = Project

        fields = [
            "title",
            "description",
            "category",
            "technologies",
            "image",
            "videos",
            "github_url",
            "live_url",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "placeholder": "Project title"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "placeholder": "Describe the project, problem solved and key results...",
                    "rows": 6
                }
            ),

            "category": forms.TextInput(
                attrs={
                    "placeholder": "e.g. Data Analytics"
                }
            ),

            "technologies": forms.TextInput(
                attrs={
                    "placeholder": "e.g. Python, Pandas, Plotly, Streamlit"
                }
            ),

            "github_url": forms.URLInput(
                attrs={
                    "placeholder": "https://github.com/username/repository"
                }
            ),

            "live_url": forms.URLInput(
                attrs={
                    "placeholder": "https://your-live-app-url.com"
                }
            ),
        }