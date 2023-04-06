

# import requests
# from unittest.mock import Mock

# def get_data_from_api(api_url):
#     response = requests.get(api_url)
#     return response.json()

# def test_get_data_from_api():
#     # Create a mock response for the API call
#     mock_response = Mock()
#     mock_response.json.return_value = {'foo': 'bar'}

#     # Patch the requests.get function to return the mock response
#     with patch('requests.get', return_value=mock_response):
#         # Call the function with the mock API response
#         result = get_data_from_api('http://example.com')

#     # Assert that the function returned the expected result
#     assert result == {'foo': 'bar'}

# # Create your tests here.



# from django.test import TestCase
# from django.utils import timezone
# from unittest.mock import patch
# from rest_framework.test import APIRequestFactory
# from .models import Book,PublishingHouse
# from .serializers import BookSerializer
# from .views import BooksByReleasingYear

# class BooksByReleasingYearTest(TestCase):
#     def setUp(self):
#         self.factory = APIRequestFactory()

#     @patch('api.views.Book.objects.all')
#     def test_filter_by_releasing_year(self, mock_book_all):
#         pHouse = PublishingHouse.objects.create(name = "fortest",headquarters = "fortest",founding_year = 2000)
#         book1 = Book.objects.create(title='Book 1',publishing_house = pHouse,description ="aaaaaa", releasing_year=2000)
#         book2 = Book.objects.create(title='Book 2', publishing_house = pHouse,description ="aaaaaa",releasing_year=2005)
#         book3 = Book.objects.create(title='Book 3', publishing_house = pHouse,description ="aaaaaa",releasing_year=2010)


#         # Create a list of book IDs
#         book_ids = [2000,2005,2010]

#         # Get the values for the book IDs
#         book_values = list(Book.objects.filter(releasing_year__in=book_ids).values_list('releasing_year', flat=True))

#         # Use the `in_bulk()` method to fetch the objects as a dictionary
#         book_dict = Book.objects.in_bulk(book_values)

#         # Create a new QuerySet from the dictionary
#         book_queryset = Book.objects.filter(id__in=book_dict.keys())


#         request = self.factory.get('findbooks/?value=2004')
#         view = BooksByReleasingYear.as_view()
#         response = view(request)
        
        
        
#         self.assertEqual(len(response.data), 2)
#         self.assertEqual(response.data[0]['title'], 'Book 2')
#         self.assertEqual(response.data[1]['title'], 'Book 3')
        
#         mock_book_all.assert_called_once()
#         mock_book_all.book_queryset.filter.assert_called_once_with(releasing_year__gt=2004)



# class Book( models.Model):
#     title = models.CharField(max_length=100,default = "")
#     #author = models.ManyToManyField(Author, through= 'BookWithAuthors')
#     publishing_house = models.ForeignKey( PublishingHouse, related_name = "books", on_delete = models.CASCADE)
#     description = models.TextField(default = "")
#     releasing_year = models.IntegerField(default = 0)
    
#     def __str__(self):
#         return self.title 




# class PublishingHouse ( models.Model):
#     name = models.CharField( max_length = 100)
#     headquarters = models.CharField ( max_length = 100)
#     founding_year = models.IntegerField(default = 0)

# from django.test import TestCase
# from rest_framework.test import APIRequestFactory
# from django.test import RequestFactory
# from unittest.mock import Mock

# from .views import BooksByReleasingYear



# class BooksByReleasingYearTest(TestCase):
#     def setUp(self):
#         self.factory = APIRequestFactory()
#     def test_my_viewset_filter():
#         # Create a mock queryset of books with release year attribute
#         mock_books = [
#             Mock(releasing_year=2019),
#             Mock(releasing_year=2020),
#             Mock(releasing_year=2021),
#         ]
#         mock_queryset = Mock(filter=Mock(return_value=mock_books))

#         # Create a mock request with query parameters for release year
#         mock_request = RequestFactory().get('/', {'releasing_year': 2020})

#         # Create a mock viewset and set the queryset
#         viewset = BooksByReleasingYear()
#         viewset.queryset = mock_queryset

#         # Call the filter_queryset method with the mock request
#         queryset = viewset.filter_queryset(mock_queryset, mock_request)

#         # Assert that the filter_queryset method returns the expected queryset
#         assert queryset.filter.called_once_with(releasing_year=2020)





# _____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________




from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from api.models import Book, PublishingHouse, Author,BookWithAuthors


class ArtByYearTest(APITestCase):
    def setUp(self):

        self.pHouse = PublishingHouse.objects.create (id = 1,name = "fortest",headquarters = "fortest",founding_year = 2000)
        self.book1 = Book.objects.create(id = 1,title='Book 1',publishing_house = self.pHouse,description ="aaaaaa", releasing_year=2000)
        self.book2 = Book.objects.create(id = 2,title='Book 2', publishing_house = self.pHouse,description ="aaaaaa",releasing_year=2005)
        self.book3 = Book.objects.create(id = 3,title='Book 3', publishing_house = self.pHouse,description ="aaaaaa",releasing_year=2010)



    def test_book_by_year(self):
        response = self.client.get('/api/findbooks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['title'], 'Book 1')

    def test_art_by_year_no_result(self):
        response = self.client.get('/api/findbooks/?value=3000')
        self.assertEqual(response.status_code,  status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)



class AuthorsByAvgReleasingYearOfTheirBooksTets(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.author1 = Author.objects.create(
            id=1, first_name='liviu',last_name = "rebreanu" ,nationality ="romanian", date_of_birth= 1885,preponderent_genre = "novels")
            
        
        self.author2 = Author.objects.create(
            id=2, first_name='george',last_name = "calinescu" ,nationality ="romanian", date_of_birth= 1900,preponderent_genre = "novels")
        

        self.pHouse = PublishingHouse.objects.create (id = 1,name = "fortest",headquarters = "fortest",founding_year = 2000)
        self.book1 = Book.objects.create(id = 1,title='Book 1',publishing_house = self.pHouse,description ="aaaaaa", releasing_year=2000)
        self.book2 = Book.objects.create(id = 2,title='Book 2', publishing_house = self.pHouse,description ="aaaaaa",releasing_year=2005)
        self.book3 = Book.objects.create(id = 3,title='Book 3', publishing_house = self.pHouse,description ="aaaaaa",releasing_year=2010)


        self.relation1 = BookWithAuthors.objects.create(id = 1,book = self.book1, author = self.author1,book_contribution = "sasasasa", author_additions = "sdkjhgfjsd" )
        self.relation2 = BookWithAuthors.objects.create(id = 2,book = self.book1,author = self.author2,book_contribution = "sasasasa", author_additions = "sdkjhgfjsd" )

        self.relation3 = BookWithAuthors.objects.create(id = 3,book = self.book2,author = self.author1,book_contribution = "sasasasa", author_additions = "sdkjhgfjsd" )
        self.relation4 = BookWithAuthors.objects.create(id = 4,book = self.book3,author = self.author2,book_contribution = "sasasasa", author_additions = "sdkjhgfjsd" )

    def test_AuthorsByAvgReleasingYearOfTheirBooks(self):
        response = self.client.get('/api/authors-by-avg-releasing-year/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['first_name'], 'liviu')
        self.assertEqual(response.data[0]['avg_releasing_year'], 2002.5)

        self.assertEqual(response.data[1]['first_name'], 'george')
        self.assertEqual(response.data[1]['avg_releasing_year'], 2005)


class PublishingHousesByTheNumberOfBooksTheyHaveTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.pHouse1 = PublishingHouse.objects.create (id = 1,name = "fortest1",headquarters = "fortest",founding_year = 2000)
        self.pHouse2 = PublishingHouse.objects.create (id = 2,name = "fortest2",headquarters = "fortest",founding_year = 2000)
       

        self.book1 = Book.objects.create(id = 1,title='Book 1',publishing_house = self.pHouse1,description ="aaaaaa", releasing_year=2000)
        self.book2 = Book.objects.create(id = 2,title='Book 2', publishing_house = self.pHouse2,description ="aaaaaa",releasing_year=2005)
        self.book3 = Book.objects.create(id = 3,title='Book 3', publishing_house = self.pHouse2,description ="aaaaaa",releasing_year=2010)


    def test_PublishingHousesByTheNumberOfBooksTheyHave(self):
        response = self.client.get('/api/publishing-houses/count-smth/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'fortest1')
        # self.assertEqual(response.data[0]['books'].len(), 1)

        self.assertEqual(response.data[1]['name'], 'fortest2')
        # self.assertEqual(response.data[0]['books'].len(), 2)







       
