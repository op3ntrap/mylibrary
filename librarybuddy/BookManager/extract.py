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
            authors = author + "," + authors
        authors = authors[0:-1]
        # i=0
        # for val in meta_data.keys():
        #     t = google_books_data[kickstr[i]]
        #     if val == 'cover':
        #         t = google_books_data['imageLinks']['thumbnail']
        #     elif val == 'published_date':
        #         t=
        #     meta_data[val] = t
        #     i+=1
        meta_data = {
            'google_url'    : "",
            'description'   : "",
            'tags'          : "",
            'cover'         : "",
            'published_date': "",
            'publisher'     : "",
            'authors'       : "",
            'page_count'    : "",
            'title'         : ""
        }
        try:
            meta_data['google_url'] = google_books_data['canonicalVolumeLink']
        except:
            meta_data['google_url'] = None
        try:
            meta_data['description'] = google_books_data['description']
        except:
            meta_data['description'] = None
        try:
            meta_data['tags'] = google_books_data['categories']
        except:
            meta_data['tags'] = None
        try:
            meta_data['cover'] = google_books_data['imageLinks']['thumbnail']
        except:
            meta_data['cover'] = None
        try:
            meta_data['published_date'] = parser.parse(google_books_data['publishedDate'])
        except:
            meta_data['published_date'] = None
        try:
            meta_data['publisher'] = google_books_data['publisher']
        except:
            meta_data['publisher'] = None
        try:
            meta_data['authors'] = authors
        except:
            meta_data['authors'] = None
        try:
            meta_data['page_count'] = google_books_data['pageCount']
        except:
            meta_data['page_count'] = None
        try:
            meta_data['title'] = google_books_data['title']
        except:
            meta_data['title'] = "Title"
        print(meta_data)
        print(google_books_data)
        return meta_data


class Integrate:
    pass


if __name__ == "__main__":
    isbn = "9781491962299"
