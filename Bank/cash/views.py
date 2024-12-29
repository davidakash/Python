from rest_framework import viewsets
# from rest_framework.response import Response
from .models import *
from .serializers import *

class BankProducts(viewsets.ModelViewSet):
    # def get(self,request):
    #     values = lucky.objects.all()
    #     json_format = lucky_serializers(values, many = True).data
    #     return Response(json_format)
    queryset = lucky.objects.all()
    serializer_class = lucky_serializers

class acc(viewsets.ModelViewSet):
    queryset = boss.objects.all()
    serializer_class = boss_serializers


    # def post(self,request):
    #    new_data = lucky_serializers(data = request.data)
    #    if new_data.is_valid():
    #     new_data.save()
    #    return Response('Data saved')
    
# class json_data(APIView):
#     def delete(self,request,id):
#         del_data = lucky.objects.get(id = id)
#         del_data.delete()
#         return Response("Deleted")

    # def patch(self,request,id):
    #     update_data = lucky.objects.filter(id = id)
    #     update_data.update(Name=request.data['Name'],AccNo = request.data['AccNo'])
    #     return Response("UPDATED SUCESSFULLY")        

    
