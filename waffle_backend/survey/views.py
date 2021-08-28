from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404

from survey.serializers import *


def get_survey_results(request):
    if request.method == 'GET':
        params = request.GET.get('os')
        if params not in ['Windows', 'MacOS', 'Linux']:
            return JsonResponse(None, status=400, safe=False)
        if params is None:
            data = SurveyResult.objects.all()
        else:
            data = SurveyResult.objects.filter(os__name=params)
        survey_results = list(map(lambda result: serialize_survey_result(result), data))
        return JsonResponse({"surveys": survey_results}, status=200)
    else:
        return HttpResponseNotAllowed(['GET', ])


def get_survey(request, survey_id):
    if request.method == 'GET':
        survey = get_object_or_404(SurveyResult, id=survey_id)
        return JsonResponse(serialize_survey_result(survey))
    else:
        return HttpResponseNotAllowed(['GET', ])

def list_all_os(request):
    if request.method == 'GET':
        data = [serialize_os(os) for os in OperatingSystem.objects.all()]
        return JsonResponse(data, status=200, safe=False)
    else:
        return HttpResponseNotAllowed(['GET', ])

def get_os(request, os_id):
    if request.method == 'GET':
        try:
            data = serialize_os(OperatingSystem.objects.get(pk=os_id))
        except OperatingSystem.DoesNotExist:
            data = None
            return JsonResponse(data, status=404, safe=False)
        else:
            return JsonResponse(data, status=200)
    else:
        return HttpResponseNotAllowed(['GET', ])