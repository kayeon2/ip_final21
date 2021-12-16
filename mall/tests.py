from django.test import TestCase, Client
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from .models import Item

class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_trump = User.objects.create_user(username='trump', password='somepassword')
        self.user_obama = User.objects.create_user(username='obama', password='somepassword')

    def navbar_test(self, soup):
        navbar = soup.nav
        self.assertIn('Shop', navbar.text)
        self.assertIn('About Us', navbar.text)

        logo_btn = navbar.find('a', text='Navbar')
        self.assertEqual(logo_btn.attrs['href'], '/')

        home_btn = navbar.find('a', text='Home')
        # self.assertEqual(home_btn.attrs['href'], '/')

        mall_btn = navbar.find('a', text='Shop')
        # self.assertEqual(mall_btn.attrs['href'], '/mall/')

        about_me_btn = navbar.find('a', text='About Us')
        # self.assertEqual(about_me_btn.attrs['href'], '/about_me/')

    def test_item_list(self):
        response = self.client.get('/mall/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'Mall')
        self.assertEqual(Item.objects.count(), 0)

        main_area = soup.find('div', id='main-area')
        self.assertIn('아직 상품이 없습니다.', main_area.text)
        self.navbar_test(soup)
        item_001 = Item.objects.create(
           title='첫 번째 상품입니다',
           content='Hello World!',
           price='30000원',
           author=self.user_trump
        )
        item_002 = Item.objects.create(
           title='두 번째 상품입니다',
           content='두 번째',
           price='20000원',
           author=self.user_obama
        )
        self.assertEqual(Item.objects.count(), 2)

        response = self.client.get('/mall/')
        # soup = BeautifulSoup(response.content, 'html.parser')
        # #
        # self.assertEqual(response.status_code, 200)
        # main_area = soup.find('div', id='main-area')
        #
        # self.assertIn(item_001.title, main_area.text)
        # self.assertIn(item_002.title, main_area.text)
        #
        # self.assertNotIn('아직 상품이 없습니다.', main_area.text)

