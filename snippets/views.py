from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from snippets import serializers
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        Snippets = Snippet.objects.all()
        serializer = SnippetSerializer(Snippets, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try: 
            snippet = Snippet.objects.filter(pk=pk).first()
        except Snippet.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk=pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk=pk)
        serializer = SnippetSerializer(snippet, data=requeset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
