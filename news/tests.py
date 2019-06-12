from django.test import TestCase
from .models import Editor,Article, tags
import datetime as dt

# Create your tests here.
class EditorTestCaseClass(TestCase):
    # set up method
    def setUp(self):
        self.Umar = Editor(first_name = 'Umar',last_name = 'Ngare',email = 'uomarearlie7@gmail.com')
        self.Hafsa = Editor(first_name = 'Hafsa',last_name= 'Ngare', email = 'haffy@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.Umar,Editor))
# creating tests for saving functionality.
    
    def test_save_method(self):
        self.Umar.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    def test_delete_method(self):
        self.Umar.save_editor()
        self.Hafsa.save_editor()
        self.Umar.delete_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) == 1)

class ArticleTestCaseClass(TestCase):
    def setUp(self):
        # Creating a new editor and saving it
        self.James = Editor(first_name = 'James',last_name = 'Muriuki',email = 'james@moringaschool.com')
        self.James.save()

        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article = Article(title = 'Test Article',post = 'This is a random test post',editor = self.James)
        self.new_article.save()
        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
    
    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news) > 0)
    
    def test_get_news_by_date(self):
        test_date = '2017-03-17' # giving a format even spaces are a factor and affect the outcome.
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date)== 0)