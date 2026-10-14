from django.test import TestCase
from homepage.models import Article

class ArticleFixtureTestCase(TestCase):
    # Reference the fixture file name (without extension)
    fixtures = ['initial_data']

    def test_articles_loaded_correctly(self):
        # Verify total articles loaded
        self.assertEqual(Article.objects.count(), 5)

    def test_parler_translations(self):
        # Fetch an article that has multiple language translations (pk=5)
        article = Article.objects.get(pk=5)

        # Test active language switching and translation fetching
        article.set_current_language('en')
        self.assertEqual(article.title, "English: localization article")

        article.set_current_language('es')
        self.assertEqual(article.title, "Artículo de localización")

        article.set_current_language('fr')
        self.assertEqual(article.title, "Article de localisation")

    def test_safe_translation_getter(self):
        # Test your model's custom __str__ fallback logic
        article = Article.objects.get(pk=1)
        self.assertEqual(str(article), "localization article")