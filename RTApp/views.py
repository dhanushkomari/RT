from django.shortcuts import render
from .models import Standard, Section, Detail
from django.http import HttpResponse

from .serializers import DetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

def SeleceStdView(request):
    s = Standard.objects.all()
    print('s is ', s)
    return render(request, 'RTApp/std.html',{'s':s})

def SectionView(request, std_id):
    sec = Section.objects.filter(standard__std_id__iexact = std_id)
    cls = Standard.objects.get(std_id = std_id)
    print(sec)
    return render(request, 'RTApp/sec.html', {'sec':sec, 'cls':cls})



####################################################################################
#############################      REST API VIEWS     ##############################
####################################################################################

@api_view(['GET'])
def recentDetail(request):
    d = Detail.objects.all().latest('pk')
    serializer = DetailSerializer(d, many = False)
    return Response(serializer.data)


