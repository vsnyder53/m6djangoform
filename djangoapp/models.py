from django.db import models

class Form(models.Model):
    # 1. Define the choice classes correctly with actual choices inside them
    class ClassStandingChoices(models.TextChoices):
        FRESHMAN = 'FR', 'Freshman'
        SOPHOMORE = 'SO', 'Sophomore'
        JUNIOR = 'JR', 'Junior'
        SENIOR = 'SR', 'Senior'

    class MajorChoices(models.TextChoices):
        CS = 'CS', 'Computer Science'
        IT = 'IT', 'Information Technology'
        SE = 'SE', 'Software Engineering'
        DS = 'DS', 'Data Science'

    # 2. Assign your fields using these choices
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    
    major = models.CharField(
        max_length=2,
        choices=MajorChoices.choices,
        default=MajorChoices.CS
            )
    
    class_standing = models.CharField(
        max_length=2,
        choices=ClassStandingChoices.choices,
        default=ClassStandingChoices.FRESHMAN
    )
    
    # Note: Many-to-Many strings (for language checkboxes) or text fields
    languages = models.CharField(max_length=200, help_text="Comma-separated languages")
    graduation_year = models.IntegerField()
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.student_name