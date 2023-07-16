from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

import json

from .models import Post

# Create your tests here.
class BlogTest(TestCase):
    @classmethod    
    def setUpTestData(cls) -> None:
        cls.author = get_user_model().objects.create_user(
            username = "username",
            email = "email@test.com",
            password = "big secret"
        )
        cls.post = Post.objects.create(
            title = "A title for my post.",
            author = cls.author, 
            body = "Here comes the body of the blog ..."
        )
    
    def test_post_model(self):
        self.assertEqual(self.post.title, "A title for my post.")
        self.assertEqual(self.post.author, self.author)
        self.assertEqual(self.post.body, "Here comes the body of the blog ...")
        self.assertEqual(self.post.author.username, "username")
        self.assertEqual(self.author.username, "username")
        self.assertEqual(self.post.author.email, "email@test.com")
        self.assertEqual(self.author.email, "email@test.com")
        #self.assertEqual(self.post.author.password, "big secret")
        # AssertionError: 'pbkdf2_sha256$320000$hAlBMbjAiLW3r1jpXCIG[43 chars]6EA=' != 'big secret'
        self.assertEqual(self.post.get_absolute_url(), "/blabal/1/")

    def test_url_exists_at_correct_location_listview(self):
        response1 = self.client.get("")
        self.assertEqual(response1.status_code, 200)
        response2 = self.client.get("/")
        self.assertEqual(response2.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/blabal/1/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_templateview(self):
        response = self.client.get("/about-us/")
        self.assertEqual(response.status_code, 200)
    
    def test_post_listview(self):
        response = self.client.get(reverse("blog_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bloglistview.html")
        self.assertContains(response, "Blog list view - Blog app")
    
    def test_post_aboutview(self):
        response = self.client.get(reverse("blog_about_us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "aboutus.html")
        self.assertContains(response, "Contents info about us")
    
    def test_post_detailview(self):
        response = self.client.get(reverse("blog_detail", kwargs={"pk": self.post.pk}))
        no_response1 = self.client.get(reverse("blog_detail", kwargs={"pk": 1234}))
        #no_response2 = self.client.get(reverse("blog_detail", args="1234"))
        # django.urls.exceptions.NoReverseMatch: Reverse for 'blog_detail' with arguments '('1', '2', '3', '4')' not found. 1 pattern(s) tried: ['blabal/(?P<pk>[0-9]+)/\\Z']
        #no_response3 = self.client.get(reverse("blog_detail", args=1234))
        # TypeError: Value after * must be an iterable, not int
        no_response4 = self.client.get(reverse("blog_detail", args=[1234]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response1.status_code, 404)
        self.assertEqual(no_response4.status_code, 404)
        self.assertTemplateUsed(response, "blogdetailview.html")
        self.assertContains(response, "A title for my post.")
        self.assertContains(response, "Here comes the body of the blog ...")
        self.assertContains(response, "username")
        print("-------")
        content = response.content
        print(content)
        print("-------")
        print(response.templates)
        print("-------")
        print(response.context)
        print("-------")
        print(response.charset)
        print("-------")
        print("TYPE: ", type(response))
        print("-------")
        #result = json.loads(response.content)
        #print(result) # json.decoder.JSONDecodeError: Expecting value: line 2 column 1 (char 1)
        print("-------")
    
    def test_post_createview(self):
        response = self.client.post(reverse("blog_create"), {
            "title": "new title",
            "author": self.author.id,
            "body": "new content",
        })
        self.assertEqual(response.status_code, 302)
        #self.assertTemplateUsed(response, "blogcreateview.html")
        # No templates used to render the response
        self.assertEqual(Post.objects.last().title, "new title")
        self.assertEqual(Post.objects.last().body, "new content")

    def test_post_updateview(self):
        response = self.client.post(reverse("blog_update", kwargs={"pk": 1}), {
            "title": "updated title",
            "body": "updated body",
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "updated title")
        self.assertEqual(Post.objects.last().body, "updated body")

    def test_post_deleteview(self):
        response = self.client.post(reverse("blog_delete", args='1'))
        self.assertEqual(response.status_code, 302)


