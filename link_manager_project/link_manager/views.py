import requests
from bs4 import BeautifulSoup
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Collection
from .models import Link
from .serializers import CollectionSerializer, LinkSerializer


def extract_link_data(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        og_title = soup.find('meta', property='og:title')
        og_description = soup.find('meta', property='og:description')
        og_image = soup.find('meta', property='og:image')

        if not og_title:
            title = soup.title.text.strip() if soup.title else ''
        else:
            title = og_title.get('content')

        if not og_description:
            description = ''
        else:
            description = og_description.get('content')

        if not og_image:
            image = ''
        else:
            image = og_image.get('content')

        return title, description, image
    except Exception as e:
        print(f"Error extracting data from URL: {e}")
        return '', '', ''


class CreateLinkAPIView(APIView):
    def post(self, request):
        url = request.data.get('url', '')

        title, description, image = extract_link_data(url)

        link_data = {
            'user': request.user.id,
            'title': title,
            'description': description,
            'url': url,
            'image': image
        }

        serializer = LinkSerializer(data=link_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LinkDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class CollectionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CollectionListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Collection.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LinkListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LinkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Link.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
