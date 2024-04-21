import requests
from bs4 import BeautifulSoup
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Collection
from .models import Link
from .serializers import CollectionSerializer
from .serializers import LinkSerializer


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


class LinkListCreateAPIView(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class LinkDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class CollectionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CollectionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
