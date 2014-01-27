import pysolr
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from rest_framework.response import Response
from django.shortcuts import render

__author__ = 'noahsark'

solr = pysolr.Solr('http://localhost:8983/solr/abc')

class SearchSerializer(serializers.Serializer):
    location = serializers.RegexField("[0-9]+\.[0-9]+,[0-9]+\.[0-9]+", required=True)


@api_view(['GET'])
def search(request):
    '''
    # Method: GET
    ## Parameters:
    - 
    '''
    if request.method == 'GET':
        serializer = SearchSerializer(data=request.GET)
        if serializer.is_valid():
            if serializer.data['location'] is not None:
                dic = {'pt': serializer.data['location'], 'sfield': 'location',
                       'sort': 'geodist() asc'}
                results = [i for i in solr.search('*:*', **dic)]
                return Response(results, status=status.HTTP_201_CREATED)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
