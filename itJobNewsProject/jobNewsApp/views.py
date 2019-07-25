from django.shortcuts import render
from jobNewsApp.models import pubeJobs
# Create your views here.
def index_view(request):
    return render(request,"jobNewsApp/index.html")

def puneJobs_view(request):
    puneJobs_list=pubeJobs.objects.order_by('date')

    return render(request,"jobNewsApp/punejobs.html",{'puneJobs_list':puneJobs_list})
