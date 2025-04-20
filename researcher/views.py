from django.shortcuts import render
from django.views.generic import View

from researcher.methods import generate_business_profile, generate_queries, research
from researcher.task import process_research


class IndexView(View):
    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        company_name = request.POST.get("company_name")

        process_research(company_name)

        return render(request, "index.html")
