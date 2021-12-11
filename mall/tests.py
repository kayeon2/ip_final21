from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Item

class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_item_list(self):
        response = self.client.get('/mall/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'Mall')
        navbar = soup.nav
        self.assertIn('Shop', navbar.text)
        self.assertIn('About Us', navbar.text)
        self.assertEqual(Item.objects.count(), 0)

        main_area = soup.find('div', id='main-area')
        self.assertIn('아직 상품이 없습니다.', main_area.text)

        #item_001 = Item.objects.create(
        #    title='첫 번째 상품입니다',
        #    content='Hello World!',
        #)
        #item_002 = Item.objects.create(
        #    title='두 번째 상품입니다',
        #    content='두 번째',
        #)
        #self.assertEqual(Item.objects.count(), 2)

        #response = self.client.get('/mall/')
        #soup = BeautifulSoup(response.content, 'html.parser')
        #self.assertEqual(response.status_code, 200)
        #main_area = soup.find('div', id='main-area')
        #self.assertIn(item_001.title, main_area.text)
        #self.assertIn(item_002.title, main_area.text)
        #self.assertNotIn('아직 상품이 없습니다.', main_area.text)