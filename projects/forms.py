from django import forms
from .models import Project, Review, ContactMessage


class ProjectForm(forms.ModelForm):

    class Meta:

        model = Project

        fields = [
            "title",
            "description",
            "problem",
            "approach",
            "results",
            "business_impact",
            "category",
            "technologies",
            "image",
            "video",
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

            "problem": forms.Textarea(
                attrs={
                    "placeholder":
                        "What business or technical problem did this project solve?",
                    "rows": 5
                }
            ),

            "approach": forms.Textarea(
                attrs={
                    "placeholder":
                        "Explain your approach, methodology and development process.",
                    "rows": 5
                }
            ),

            "results": forms.Textarea(
                attrs={
                    "placeholder":
                        "What did your analysis, model or application achieve?",
                    "rows": 5
                }
            ),

            "business_impact": forms.Textarea(
                attrs={
                    "placeholder":
                        "How could this solution help a business, user or organization?",
                    "rows": 5
                }
            ),

            "category": forms.Select(
                attrs={
                    "class": "form-select"
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




class ReviewForm(forms.ModelForm):

    class Meta:

        model = Review

        fields = [
            "name",
            "rating",
            "comment",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "class": "review-input",
                    "placeholder": "Your Name",
                }
            ),

            "rating": forms.HiddenInput(),

            "comment": forms.Textarea(
                attrs={
                    "class": "review-textarea",
                    "placeholder": "Share your thought about this project...",
                    "rows": 5,
                }
            ),
        }

    def clean_name(self):

        name = self.cleaned_data["name"].strip()

        if len(name) < 2:

            raise forms.ValidationError(
                "Please enter your name."
            )

        return name


    def clean_comment(self):

        comment = self.cleaned_data["comment"].strip()

        if len(comment) < 5:

            raise forms.ValidationError(
                "Please write a little more about your experience."
            )

        if len(comment) > 1000:

            raise forms.ValidationError(
                "Your review cannot exceed 1000 characters."
            )

        return comment


    def clean_rating(self):

        rating = self.cleaned_data.get("rating")

        if rating is None:

            raise forms.ValidationError(
                "Please select a rating."
            )

        if rating < 1 or rating > 5:

            raise forms.ValidationError(
                "Rating must be between 1 and 5."
            )

        return rating


    
class ContactForm(forms.ModelForm):

    class Meta:

        model = ContactMessage

        fields = [
            "name",
            "email",
            "subject",
            "message",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "placeholder": "Your full name"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "your@email.com"
                }
            ),

            "subject": forms.TextInput(
                attrs={
                    "placeholder": "What would you like to discuss?"
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "placeholder":
                        "Tell me about your project, business problem or opportunity...",
                    "rows": 7
                }
            ),
        }