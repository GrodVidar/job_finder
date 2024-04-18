import datetime

from django.shortcuts import render
from django.views import generic
from apps.finder.models import JobPost, Experience, Education, Skill, JobPostQuery
import requests
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin


def call_api(query):
    url = "https://jsearch.p.rapidapi.com/search"
    querystring = {"query": query, "page": "1", "num_pages": "1"}
    headers = {
        "X-RapidAPI-Key": settings.API_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()


def create_model_instance(data, job_post_query):
    for item in data['data']:
        experience, _ = Experience.objects.get_or_create(**item.pop('job_required_experience'))
        education, _ = Education.objects.get_or_create(**item.pop('job_required_education'))
        skill_texts = item.pop('job_required_skills')
        filtered_data = {k: v for k, v in item.items() if k in [f.name for f in JobPost._meta.get_fields()]}
        job_post, _ = JobPost.objects.get_or_create(
            job_required_experience=experience,
            job_required_education=education,
            **filtered_data
        )
        job_post_query.job_posts.add(job_post)
        if skill_texts:
            for skill_text in skill_texts:
                skill, _ = Skill.objects.get_or_create(text=skill_text)
                job_post.job_required_skills.add(skill)


class JobPostsView(LoginRequiredMixin, generic.ListView):
    model = JobPostQuery
    template_name = 'finder/index.html'
    context_object_name = 'job_post_queries'

    def get_queryset(self):
        queries = self.request.user.queries.all()
        for query in queries:
            if query.last_call is None or query.last_call < datetime.date.today():
                if query.last_call:
                    JobPostQuery.objects.filter(query=query).delete()
                job_post_query = JobPostQuery.objects.create(query=query)
                api_data = call_api(query.text)
                create_model_instance(api_data, job_post_query)
                query.last_call = datetime.date.today().strftime('%Y-%m-%d')
                query.save()
        return JobPostQuery.objects.filter(query__in=queries)
