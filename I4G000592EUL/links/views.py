from django.shortcuts import generic
from models import Links

class PostListAPI(generic. ListAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateAPI(generic.CreateAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDetailAPI(generic.RetrieveAPIView): 
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateAPI(generic. UpdateAPIView):
     queryset = Links.objects.filter(active=True)
     serializer_class = LinkSerializer

class postDeleteAPI(generic.DestroyAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer


       



 
