from django.test import TestCase
from .forms import OpinionForm


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        opinion_form = OpinionForm({'your_opinion': 'This is a great band'})
        self.assertTrue(opinion_form.is_valid())
