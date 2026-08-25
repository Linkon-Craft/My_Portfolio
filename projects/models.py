from django.db import models


class Category(models.TextChoices):
    DATA_ANALYTICS = "DT_ANALYTICS", "Data_Analytics"
    MACHINE_LEARNING = "MCHINE_LEARNIN", "Machine_Learning"
    DJANGO = "DJNGO", "Django"




class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    problem = models.TextField(blank=True)
    approach = models.TextField(blank=True)
    results = models.TextField(blank=True)
    business_impact = models.TextField(blank=True)
    technologies = models.CharField(max_length=300)
    category = models.CharField(max_length=100, choices=Category.choices, default=Category.DATA_ANALYTICS)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to="proj_images/", blank=True)
    video = models.FileField(upload_to="proj_videos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f" {self.title} {self.live_url}"


class Review(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="reviews")

    name = models.CharField(max_length=100)

    rating = models.PositiveSmallIntegerField()

    comment = models.TextField()

    approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        if self.rating is None:
            raise ValueError(
                "A rating is required."
            )

        if self.rating < 1 or self.rating > 5:
            raise ValueError(
                "Rating must be between 1 and 5."
            )

        super().save(*args, **kwargs)

    def __str__(self):

        return f"{self.name} - {self.project.title}"

    class Meta:

        ordering = ["-created_at"]


class ContactMessage(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):

        return f"{self.name} - {self.subject}"