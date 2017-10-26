# https://www.googleapis.com/books/v1/volumes?q=isbn:9781603091794
import json
from urllib.request import urlopen
from dateutil import parser


class Extractor:
    def __init__(self, a, b):
        self.identifier = a
        self.identifier_value = b

    def google_books(self):
        url = "https://www.googleapis.com/books/v1/volumes?q={}:{}".format(
                self.identifier, self.identifier_value)
        return url

    def download(self):
        response = urlopen(self.google_books()).read().decode('utf8')
        json_data = json.loads(response)
        return json_data

    def metadata(self):
        """
        Combines the data from both the resources and returns the most valid metadata for the book.
        :return:(dict) metadata
        """
        # identifiers
        dump = self.download()
        if dump['totalItems'] == 0:
            return 0

        google_books_data = dump['items'][0]['volumeInfo']
        authors = ""
        for author in google_books_data['authors']:
            authors += author

        meta_data = {
            'google_url'    : google_books_data['canonicalVolumeLink'],
            'description'   : google_books_data['description'],
            'tags'          : google_books_data['categories'],
            'cover'         : google_books_data['imageLinks']['thumbnail'],
            'published_date': parser.parse(google_books_data['publishedDate']),
            'publisher'     : google_books_data['publisher'],
            'authors'       : authors,
            'page_count'    : google_books_data['pageCount'],
            'title'         : google_books_data['title']
        }
        return meta_data


class Integrate:
    pass


if __name__ == "__main__":
    isbn = "9781491962299"