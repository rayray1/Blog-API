# import generics from DRF
from rest_framework import generics

from . import models
from . import serializers




class PostList(generics.ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
