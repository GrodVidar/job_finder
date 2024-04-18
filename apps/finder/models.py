from django.db import models
from apps.users.models import Query


class Skill(models.Model):
    text = models.CharField(max_length=255, null=True)


class Education(models.Model):
    postgraduate_degree = models.BooleanField(null=True)
    professional_certification = models.BooleanField(null=True)
    high_school = models.BooleanField(null=True)
    associates_degree = models.BooleanField(null=True)
    bachelors_degree = models.BooleanField(null=True)
    degree_mentioned = models.BooleanField(null=True)
    degree_preferred = models.BooleanField(null=True)
    professional_certification_mentioned = models.BooleanField(null=True)


class Experience(models.Model):
    no_experience_required = models.BooleanField(null=True)
    required_experience_in_months = models.IntegerField(null=True)
    experience_mentioned = models.BooleanField(null=True)
    experience_preferred = models.BooleanField(null=True)


class JobPost(models.Model):
    job_id = models.CharField(max_length=255, null=True)
    employer_name = models.CharField(max_length=255,  null=True)
    employer_logo = models.URLField(null=True)
    employer_website = models.URLField(null=True)
    employer_company_type = models.CharField(max_length=255, null=True)
    job_publisher = models.CharField(max_length=255, null=True)
    job_employment_type = models.CharField(max_length=255, null=True)
    job_title = models.CharField(max_length=255, null=True)
    job_apply_link = models.URLField(null=True)
    job_apply_is_direct = models.BooleanField(null=True)
    job_apply_quality_score = models.FloatField(null=True)
    job_description = models.TextField(null=True)
    job_is_remote = models.BooleanField(null=True)
    job_posted_at_timestamp = models.IntegerField(null=True)
    job_posted_at_datetime_utc = models.DateTimeField(null=True)
    job_city = models.CharField(max_length=255, null=True)
    job_state = models.CharField(max_length=255, null=True)
    job_country = models.CharField(max_length=255, null=True)
    job_offer_expiration_timestamp = models.IntegerField(null=True)
    job_offer_expiration_datetime_utc = models.DateTimeField(null=True)
    job_required_experience = models.ForeignKey(Experience, null=True, on_delete=models.CASCADE)
    job_required_skills = models.ManyToManyField(Skill)
    job_required_education = models.ForeignKey(Education, null=True, on_delete=models.CASCADE)
    job_min_salary = models.IntegerField(null=True)
    job_max_salary = models.IntegerField(null=True)
    job_salary_currency = models.CharField(max_length=255, null=True)


class JobPostQuery(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    job_posts = models.ManyToManyField(JobPost)
