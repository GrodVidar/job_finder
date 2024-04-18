from django.db.models.signals import post_delete
from django.dispatch import receiver
from apps.finder.models import JobPostQuery, JobPost


@receiver(post_delete, sender=JobPostQuery)
def delete_related_job_posts(sender, instance, **kwargs):
    instance.job_posts.all().delete()


@receiver(post_delete, sender=JobPost)
def delete_related_experience_skills_educations(sender, instance, **kwargs):
    instance.job_required_experience.delete()
    instance.job_required_education.delete()
    instance.job_required_skills.all().delete()
