from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.test import TestCase

from .models import Post


class BlogTests(TestCase):

	def setUp(self):
		self.user = User.objects.create(username='test')

	def create_post(self, title="Test Blog Post", published=True):
		return Post.objects.create(
			title=title,
			author=self.user,
			text="test")

	def test_created_post(self):
		post = Post.objects.get(author='taras')
		self.assertEqual(post.author, 'taras')