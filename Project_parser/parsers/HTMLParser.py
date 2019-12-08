from bs4 import BeautifulSoup
from Project_parser.parsers.Parser import Parser


class HTMLParser(Parser):
    """
    Parses all text and links from HTML.
    Constructor args: filepath.
    """
    def __init__(self, filepath=None, text=None):
        if filepath:
            with open(filepath, 'rb') as file:
                self.bs = BeautifulSoup(file.read(), 'html.parser')
        if text:
            self.bs = BeautifulSoup(text, 'html.parser')

    def get_text(self):
        return self.bs.get_text()

    def get_links(self):
        links = []
        for link in self.bs.find_all('a'):
            links.append(link.get('href'))
        return links
