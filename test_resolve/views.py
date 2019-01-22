import csv

from django.http import HttpResponseNotFound
from rest_framework.response import Response
from rest_framework.views import APIView


class ListData(APIView):

    @staticmethod
    def get(request):
        url = "test_resolve/documents/Absenteeism_at_work_AAA/Absenteeism_at_work.csv"
        reader = csv.DictReader(open(url), delimiter=";")
        dict_list = []
        for line in reader:
            dict_list.append(line)

        if dict_list:
            return Response(dict_list)
        else:
            return HttpResponseNotFound({})
