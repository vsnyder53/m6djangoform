from django import forms

class StudentForm(forms.Form):
    # Drop-down choices
    MAJOR_CHOICES = [
        ('cs', 'Computer Science'),
        ('it', 'Information Technology'),
        ('se', 'Software Engineering'),
        ('ds', 'Data Science'),
    ]
    
    # Radio button choices
    STANDING_CHOICES = [
        ('fr', 'Freshman'),
        ('so', 'Sophomore'),
        ('jr', 'Junior'),
        ('sr', 'Senior'),
    ]
    
    # Checkbox choices
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
      ('java', 'Java'),
        ('cpp', 'C++'),
        ('javascript', 'JavaScript'),
    ]

    # Form Fields & Widgets
    student_name = forms.CharField(label="Student Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    student_id = forms.CharField(label="Student ID", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    major = forms.ChoiceField(label="Major", choices=MAJOR_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    
    class_standing = forms.ChoiceField(
        label="Class Standing", 
        choices=STANDING_CHOICES, 
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
            )
    
    languages = forms.MultipleChoiceField(
        label="Programming Languages Known",
        choices=LANGUAGE_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    )
    
    graduation_year = forms.IntegerField(label="Expected Graduation Year", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    comments = forms.CharField(label="Comments", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    