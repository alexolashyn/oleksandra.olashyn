from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Auto
from .serializers import AutoSerializer
from django.shortcuts import get_object_or_404


# Create your views here.

class AutoView(APIView):

    def get(self, request, id=False):
        if id:
            try:
                result = Auto.objects.get(id=id)
                serializers = AutoSerializer(result)
                return Response({'success': 'success', "data": serializers.data}, status=200)
            except Auto.DoesNotExist:
                return Response({"status": "error", "data": 'no such id'}, status=status.HTTP_400_BAD_REQUEST)
        serializers = None
        marker = True
        searched = []
        if 'search' in request.query_params:
            fields = [field.name for field in Auto._meta.get_fields()]
            result = Auto.objects.all()
            for auto in result.iterator():
                for index in range(len(fields)):
                    if request.query_params['search'] in str(getattr(auto, fields[index])):
                        serializers = AutoSerializer(auto)
                        searched.append(serializers.data)
            marker = False
        if 'sort_by' in request.query_params:
            if searched:
                if 'sort_type' in request.query_params and request.query_params['sort_type'] == 'desc':
                    searched = sorted(searched, key=lambda auto: str(auto[request.query_params['sort_by']]).lower(),
                                      reverse=True)
                else:
                    searched = sorted(searched,
                                      key=lambda auto: str(auto[request.query_params['sort_by']]).lower())
            else:
                if 'sort_type' in request.query_params and request.query_params['sort_type'] == 'desc':
                    result = sorted(Auto.objects.all(),
                                    key=lambda auto: str(getattr(auto, request.query_params['sort_by'])).lower(),
                                    reverse=True)

                else:
                    result = sorted(Auto.objects.all(),
                                    key=lambda auto: str(getattr(auto, request.query_params['sort_by'])).lower())
                serializers = AutoSerializer(result, many=True)
            marker = False
        if marker:
            result = Auto.objects.all()
            serializers = AutoSerializer(result, many=True)
        if searched:
            return Response({'status': 'success', "data": searched}, status=200)
        return Response({'status': 'success', "data": serializers.data}, status=200)

    def post(self, request):
        serializer = AutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        result = Auto.objects.get(id=id)
        serializer = AutoSerializer(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        result = get_object_or_404(Auto, id=id)
        result.delete()
        return Response({"status": "success", "data": "Record Deleted"})
