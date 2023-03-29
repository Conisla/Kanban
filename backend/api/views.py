from django.shortcuts import render
from api.models import Colonne, Tache

from api.serializers import ColonneSerializer, TaskSerializer

#API 
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

class ColonneViewset(viewsets.ModelViewSet):
    queryset = Colonne.objects.all()
    serializer_class = ColonneSerializer

class TaskViewset(viewsets.ModelViewSet):
    queryset = Tache.objects.all()
    serializer_class = TaskSerializer

class BoardView(APIView):
    def get(self, request, format=None):
        # Récupération des colonnes
        colonnes = Colonne.objects.all().order_by('pos')
        colonnes_data = []
        for colonne in colonnes:
            colonne_data = ColonneSerializer(colonne).data
            # Récupération des tâches associées à la colonne
            taches = Tache.objects.filter(id_col=colonne.id_col).order_by('pos')
            taches_data = TaskSerializer(taches, many=True).data
            colonne_data['taches'] = taches_data
            colonnes_data.append(colonne_data)

        return Response(colonnes_data, status=status.HTTP_200_OK)