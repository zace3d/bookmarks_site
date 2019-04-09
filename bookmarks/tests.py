from django.test import TestCase, RequestFactory

# Create your tests here.

from django.contrib.auth.models import AnonymousUser, User
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.test import force_authenticate
from rest_framework.views import status
from .models import Bookmark
from .serializers import BookmarkSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_bookmark(url="", title="", description="", owner=""):
        if url != "" and title != "" and description != "":
            Bookmark.objects.create(url=url, title=title, description=description, owner = owner)

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='factico', email='hola@factico.com.mx', password='holamundo')
        # add test data
        self.create_bookmark("https://www.supercivicosapp.com", "Supercívicos", "ariana grande", self.user)
        self.create_bookmark("https://liguepolitico.com","Ligue Político Frontend", "konshens", self.user)
        self.create_bookmark("https://liguepolitico.org","Ligue Político Backend", "brick and lace", self.user)
        self.create_bookmark("https://www.google.com", "Google", "damien marley", self.user)


class GetAllBookmarksTest(BaseViewTest):

    def test_get_all_bookmarks(self):
        """
        This test ensures that all bookmarks added in the setUp method
        exist when we make a GET request to the bookmarks/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("bookmarks-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Bookmark.objects.all()
        serialized = BookmarkSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)