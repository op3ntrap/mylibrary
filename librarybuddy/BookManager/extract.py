# https://www.googleapis.com/books/v1/volumes?q=isbn:0735619670
import json
from urllib.request import urlopen


class Extractor:
    metadata = {}

    def __init__(self, payload):
        self.identifier = payload['identifier']
        self.identifier_value = payload['identifier_value']

    def google_books(self):
        url = "https://www.googleapis.com/books/v1/volumes?q={}:{}".format(
                self.identifier, self.identifier_value)
        print(url)
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
        google_books_data = dump['items'][0]['volumeInfo']
        meta_data = {
            'google_url'    : google_books_data['canonicalVolumeLink'],
            'description'   : google_books_data['description'],
            'tags'          : google_books_data['categories'],
            'cover'         : google_books_data['imageLinks']['thumbnail'],
            'published_date': google_books_data['publishedDate'],
            'publisher'     : google_books_data['publisher'],
            'authors'       : google_books_data['authors'],
            'page_count'    : google_books_data['pageCount'],
            'title'         : google_books_data['title']
        }
        return meta_data


class Integrate:
    pass


if __name__ == "__main__":
    isbn = "9781491962299"
    w = Extractor({'identifier': 'isbn', 'identifier_value': isbn})
    print(w.metadata())
