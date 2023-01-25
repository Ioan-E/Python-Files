import logging
import sys
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser

bbc = "https://www.bbc.com"
nbc = "https://www.nbcnews.com/latest-stories/"
fox = "https://www.foxnews.com/"
protv = "https://stirileprotv.ro/"
digi24 = "https://www.digi24.ro/"

now = datetime.now()
date_string = now.strftime("%d-%m-%Y--%H-%M")
logging.basicConfig(level=logging.DEBUG, filename=f'Python Files/For Git/News App/logs/{date_string}_log.log')
logger = logging.getLogger('NewsApp')


class FancyWrite:
    file_is_created = False

    def __enter__(self):
        now = datetime.now()
        date_string = now.strftime("%d-%m-%Y")
        logger.info(f"Attempting to open the file '{date_string}_articles.txt'")
        self.file = open(f"Python Files/For Git/News App/saved articles/{date_string}_articles.txt", "a")
        logger.debug(f"Opened the file for append")
        if not self.file_is_created:
            self.file.write(f"These are the articles you saved on {date_string}:\n")
            self.file_is_created = True
        return self

    def fancy_write(self, text, href):
        logger.info(f"Adding the header '{text}' to the file")
        self.file.write(f"{text} || ({href})")

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        logger.debug("Closed the file")


class News():
    def __init__(self):
        self.newslist = []

    def __iadd__(self, header):
        self.newslist.append(header)
        logger.debug(f'Added {header} to id[{id(self)}]')
        return self

    def __iter__(self):
        return iter(self.newslist)

    def __getitem__(self, index):
        return self.newslist[index]

    def __setitem__(self, index, item):
        self.newslist[index] = item

    def __delitem__(self, index):
        del self.newslist[index]

    def __len__(self):
        return len(self.newslist)

    def __str__(self):
        string = ''
        for item in self.newslist:
            string += str(item) + '\n'
        if len(self) == 0:
            return "Empty"
        return string[-1]

    def __repr__(self):
        string = f'{type(self).__name__} object id={id(self)}: \n'
        for item in self.newslist:
            string += repr(item) + '\n'
        return string[:-1]


class NewsMixin():
    def get_first_x_news(self, number):
        logger.info(f'Getting the first {number} headers from {self.__class__.__name__}')
        newsobj = self.__class__()                                  #returns the subclass when is called from a subclass
        news_generator = self.get_news()
        for i in range(number):
            newsobj += next(news_generator)                         #uses the generator from the class
        return newsobj


class Header():
    def __init__(self, text, href, *args):
        self.attributes = [text, href]
        self.text = text
        self.href = href
        for arg in args:
            self.attributes.append(arg)

    def __getitem__(self, index):
        return self.attributes[index]

    def __len__(self):
        return len(self.attributes)

    def __str__(self):
        string = ''
        for item in self.attributes:
            string += item + ', '
        return string[:-2]

    def __repr__(self):
        string = 'Header ('
        for item in self.attributes:
            string += item + ', '
        string = string[:-2] + f') [{id(self)}]'
        return string


class Bbc(News, NewsMixin):

    @staticmethod
    def get_all_news():
        logger.info(f'Getting ALL available news from BBC')
        page = requests.get(bbc)
        soup = BeautifulSoup(page.content, "lxml")
        bbcnews = Bbc()
        for element in soup.find_all('h3', class_='media__title'):          #html level three heading, CSS class -> media title
            atag = element.find('a')
            href = atag['href']
            if bbc not in href:
                href = bbc + href
            text = atag.text.strip()
            bbcnews += Header(text, href)
        return bbcnews

    @staticmethod                                                           #builds a generator
    def get_news():
        page = requests.get(bbc)
        soup = BeautifulSoup(page.content, "lxml")
        for element in soup.find_all('h3', class_='media__title'):
            logger.debug("Getting the next header in BBC")
            atag = element.find('a')
            href = atag['href']
            if bbc not in href:
                href = bbc + href
            text = atag.text.strip()
            yield Header(text, href)


class Nbc(News, NewsMixin):

    @staticmethod
    def get_all_news():
        logger.info(f'Getting ALL available news from NBC')
        page = requests.get(nbc)
        soup = BeautifulSoup(page.content, "lxml")
        nbcnews = Nbc()
        for element in soup.find_all('div', class_='tease-card__info'):
            atag = element.find('a')
            href = atag['href']
            text = atag.text.strip()
            nbcnews += Header(text, href)
        return nbcnews

    @staticmethod
    def get_news():
        page = requests.get(nbc)
        soup = BeautifulSoup(page.content, "lxml")
        nbcnews = Nbc()
        for element in soup.find_all('div', class_='tease-card__info'):
            logger.debug("Getting the next header in NBC")
            atag = element.find('a')
            href = atag['href']
            text = atag.text.strip()
            yield Header(text, href)


class Fox(News, NewsMixin):

    @staticmethod
    def get_all_news():
        logger.info(f'Getting ALL available news from FOX')
        page = requests.get(fox)
        soup = BeautifulSoup(page.content, "lxml")
        foxnews = Fox()
        article_list = soup.find('div', class_='collection-article-list')
        for element in article_list.find_all('h2'):
            text = element.text.strip()
            href = element.find('a')['href']
            foxnews += Header(text, href)
        return foxnews

    @staticmethod
    def get_news():
        page = requests.get(fox)
        soup = BeautifulSoup(page.content, "lxml")
        foxnews = Fox()
        article_list = soup.find('div', class_='collection-article-list')
        for element in article_list.find_all('h2'):
            logger.debug("Getting the next header in FOX")
            text = element.text.strip()
            href = element.find('a')['href']
            yield Header(text, href)


class Protv(News, NewsMixin):

    @staticmethod
    def get_all_news():
        logger.info(f'Getting ALL available news from PROTV')
        page = requests.get(protv)
        soup = BeautifulSoup(page.content, "lxml")
        protvnews = Protv()
        for element in soup.find_all('h2', class_='truncate-overflow'):
            text = element.text.strip()
            href = element.find('a')['href']
            protvnews += Header(text, href)
        return protvnews

    @staticmethod
    def get_news():
        page = requests.get(protv)
        soup = BeautifulSoup(page.content, "lxml")
        protvnews = Protv()
        for element in soup.find_all('h2', class_='truncate-overflow'):
            logger.debug("Getting the next header in PROTV")
            text = element.text.strip()
            href = element.find('a')['href']
            yield Header(text, href)


class Digi24(News, NewsMixin):

    @staticmethod
    def get_all_news():
        logger.info(f'Getting ALL available news from DIGI24')
        page = requests.get(digi24)
        soup = BeautifulSoup(page.content, "lxml")
        digi24news = Digi24()
        for element in soup.find_all('h4', class_='article-title'):
            text = element.text.strip()
            href = element.find('a')['href']
            if 'www.digi' not in href:
                href = digi24 + href[1:]
            digi24news += Header(text, href)
        return digi24news

    @staticmethod
    def get_news():
        page = requests.get(digi24)
        soup = BeautifulSoup(page.content, "lxml")
        digi24news = Digi24()
        for element in soup.find_all('h4', class_='article-title'):
            logger.debug("Getting the next header in DIGI24")
            text = element.text.strip()
            href = element.find('a')['href']
            if 'www.digi' not in href:
                href = digi24 + href[1:]
            yield Header(text, href)


class HyperLinkTextBox(QTextBrowser):
    def __init__(self, parent=None):
        super().__init__()
        self.setStyleSheet('font-size: 20px;')
        self.setOpenExternalLinks(True)
        self.setParent(parent)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(801, 673)
        self.setWindowTitle("News App")
        self.setStyleSheet("background-color: #1B262C; color: #BBE1fA;")
        self.beamCursor = QtGui.QCursor(QtCore.Qt.IBeamCursor)
        self.pointingCursor = QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        self.setupUI()
        self.alt_text = ''
        self.news_text = self.default_news()
        self.textBox.setText(self.news_text)

    def setupUI(self):
        logger.info("Setting up the GUI...")
        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setText("Hello, this is today's feed:")
        self.label_1.setGeometry(QtCore.QRect(20, 10, 241, 21))
        self.label_1.setStyleSheet("background-color: #0F4C75")
        self.label_1.setObjectName("label_1")

        self.textBox = HyperLinkTextBox(self)
        self.textBox.setGeometry(QtCore.QRect(20, 50, 451, 571))
        self.textBox.viewport().setProperty("cursor", self.beamCursor)
        self.textBox.setObjectName("textBox")

        self.textInput_1 = QtWidgets.QTextEdit(self)
        self.textInput_1.setGeometry(QtCore.QRect(590, 110, 171, 31))
        self.textInput_1.viewport().setProperty("cursor", self.beamCursor)
        self.textInput_1.setObjectName("textInput_1")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setText("Search by:")
        self.label_2.setGeometry(QtCore.QRect(500, 120, 81, 16))
        self.label_2.setObjectName("label_2")

        self.checkBox_1 = QtWidgets.QCheckBox(self)
        self.checkBox_1.setText("BBC")
        self.checkBox_1.setGeometry(QtCore.QRect(500, 160, 111, 21))
        self.checkBox_1.setCursor(self.pointingCursor)
        self.checkBox_1.setObjectName("checkBox_1")

        self.checkBox_2 = QtWidgets.QCheckBox(self)
        self.checkBox_2.setText("NBC")
        self.checkBox_2.setGeometry(QtCore.QRect(500, 190, 111, 21))
        self.checkBox_2.setCursor(self.pointingCursor)
        self.checkBox_2.setObjectName("checkBox_2")

        self.checkBox_3 = QtWidgets.QCheckBox(self)
        self.checkBox_3.setText("Fox")
        self.checkBox_3.setGeometry(QtCore.QRect(500, 220, 111, 21))
        self.checkBox_3.setCursor(self.pointingCursor)
        self.checkBox_3.setObjectName("checkBox_3")

        self.checkBox_4 = QtWidgets.QCheckBox(self)
        self.checkBox_4.setText("ProTV")
        self.checkBox_4.setGeometry(QtCore.QRect(500, 250, 111, 21))
        self.checkBox_4.setCursor(self.pointingCursor)
        self.checkBox_4.setObjectName("checkBox_4")

        self.checkBox_5 = QtWidgets.QCheckBox(self)
        self.checkBox_5.setText("Digi24")
        self.checkBox_5.setGeometry(QtCore.QRect(500, 280, 111, 21))
        self.checkBox_5.setCursor(self.pointingCursor)
        self.checkBox_5.setObjectName("checkBox_5")

        self.searchButton = QtWidgets.QPushButton(self)
        self.searchButton.setText("Search")
        self.searchButton.setGeometry(QtCore.QRect(620, 170, 111, 121))
        self.searchButton.setCursor(self.pointingCursor)
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(self.search)

        self.refreshButton = QtWidgets.QPushButton(self)
        self.refreshButton.setText("Refresh")
        self.refreshButton.setGeometry(QtCore.QRect(500, 50, 111, 40))
        self.refreshButton.setCursor(self.pointingCursor)
        self.refreshButton.setObjectName("refreshButton")
        self.refreshButton.clicked.connect(self.refresh)

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setText("Enter the numbers of the articles that interest you here:")
        self.label_3.setGeometry(QtCore.QRect(500, 370, 281, 41))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")

        self.textInput_2 = QtWidgets.QTextEdit(self)
        self.textInput_2.setGeometry(QtCore.QRect(500, 420, 271, 31))
        self.textInput_2.viewport().setProperty("cursor", self.beamCursor)
        self.textInput_2.setObjectName("textInput_2")

        self.writeButton = QtWidgets.QPushButton(self)
        self.writeButton.setText("Write")
        self.writeButton.setGeometry(QtCore.QRect(550, 470, 161, 51))
        self.writeButton.setCursor(self.pointingCursor)
        self.writeButton.setObjectName("writeButton")
        self.writeButton.clicked.connect(self.write)

    def write(self):
        logger.info("The write button has been pressed. Writing...")
        string_input = self.textInput_2.toPlainText().split(' ')
        for string in self.alt_text[:-1].split('\n'):
            index, text, href = string.split('||')
            if index in string_input:
                with FancyWrite() as fwrite:
                    fwrite.fancy_write(text, href)

    def refresh(self):
        logger.info("The refresh button has been pressed. Refreshing...")
        self.news_text = self.default_news()
        self.textBox.setText(self.news_text)

    def search(self):
        logger.info("The search button has been pressed. Searching...")
        word_input = self.textInput_1.toPlainText()
        result_string = ''
        alternate_string = ''
        index = 1
        atag = "<a style=\"color: white; text-decoration: none;\" href=\""
        if self.checkBox_1.isChecked():
            logger.info(f'Searching for {word_input} in BBC...')
            found_results = False
            result_string += "BBC:<br>"
            bbcnews = Bbc.get_all_news()
            for header in bbcnews:
                if word_input in header.text:
                    result_string += f'{atag}{header.href}\">{index}. {header.text}</a>'
                    result_string += '<br>'
                    alternate_string += f'{index}||{header.text}||{header.href}' + '\n'
                    index += 1
                    found_results = True
            if found_results is False:
                result_string += f"Couldn't find BBC articles that match {word_input}<br>"
                logger.warning(f"Couldn't find any results for {word_input} in BBC")

        if self.checkBox_2.isChecked():
            logger.info(f'Searching for {word_input} in NBC...')
            found_results = False
            result_string += "NBC:<br>"
            nbcnews = Nbc.get_all_news()
            for header in nbcnews:
                if word_input in header.text:
                    result_string += f'{atag}{header.href}\">{index}. {header.text}</a>'
                    result_string += '<br>'
                    alternate_string += f'{index}||{header.text}||{header.href}' + '\n'
                    index += 1
                    found_results = True
            if found_results is False:
                result_string += f"Couldn't find NBC articles that match {word_input}<br>"
                logger.warning(f"Couldn't find any results for {word_input} in NBC")

        if self.checkBox_3.isChecked():
            logger.info(f'Searching for {word_input} in FOX...')
            found_results = False
            result_string += "FOX:<br>"
            foxnews = Fox.get_all_news()
            for header in foxnews:
                if word_input in header.text:
                    result_string += f'{atag}{header.href}\">{index}. {header.text}</a>'
                    result_string += '<br>'
                    alternate_string += f'{index}||{header.text}||{header.href}' + '\n'
                    index += 1
                    found_results = True
            if found_results is False:
                result_string += f"Couldn't find Fox articles that match {word_input}<br>"
                logger.warning(f"Couldn't find any results for {word_input} in FOX")

        if self.checkBox_4.isChecked():
            logger.info(f'Searching for {word_input} in PROTV...')
            found_results = False
            result_string += "PROTV:<br>"
            protvnews = Protv.get_all_news()
            for header in protvnews:
                if word_input in header.text:
                    result_string += f'{atag}{header.href}\">{index}. {header.text}</a>'
                    result_string += '<br>'
                    alternate_string += f'{index}||{header.text}||{header.href}' + '\n'
                    index += 1
                    found_results = True
            if found_results is False:
                result_string += f"Couldn't find PROTV articles that match {word_input}<br>"
                logger.warning(f"Couldn't find any results for {word_input} in PROTV")

        if self.checkBox_5.isChecked():
            logger.info(f'Searching for {word_input} in DIGI24...')
            found_results = False
            result_string += "DIGI24:<br>"
            digi24news = Digi24.get_all_news()
            for header in digi24news:
                if word_input in header.text:
                    result_string += f'{atag}{header.href}\">{index}. {header.text}</a>'
                    result_string += '<br>'
                    alternate_string += f'{index}||{header.text}||{header.href}' + '\n'
                    index += 1
                    found_results = True
            if found_results is False:
                result_string += f"Couldn't find Digi24 articles that match {word_input}<br>"
                logger.warning(f"Couldn't find any results for {word_input} in DIGI24")
        self.alt_text = alternate_string
        self.news_text = result_string
        self.textBox.setText(self.news_text)

    def prettify_news(fnc):
        def inner(self):
            default_string = fnc(self).split('<br>')
            logger.info("Decorating the recieved string...")
            new_string = ''
            news_list = ["BBC", "NBC", "FOX", "PROTV", "DIGI24"]
            for string in default_string:
                if string[:-1] in news_list:
                    new_string += '~'*37 + '<br>'
                    new_string += string + '<br>'
                    new_string += '~'*37 + '<br>'
                else:
                    new_string += string + '<br>'
            return new_string
        return inner

    @prettify_news
    def default_news(self):
        logger.info("Getting the default news...")
        atag = "<a style=\"color: white; text-decoration: none;\" href=\""
        news_string = ''
        alternate_string = ''
        index = 1
        bbc = Bbc()
        bbc = bbc.get_first_x_news(5)
        nbc = Nbc()
        nbc = nbc.get_first_x_news(2)
        fox = Fox()
        fox = fox.get_first_x_news(1)
        # protv = Protv()
        # protv = protv.get_first_x_news(5)
        # digi24 = Digi24()
        # digi24 = digi24.get_first_x_news(5)
        news_string += 'BBC:<br>'
        for header in bbc:
            news_string += f'{atag}{header.href}\">{index}. {header.text}</a>'
            news_string += '<br>'
            alternate_string += f'{index}||{header.text}||{header.href}' + '\n'
            index += 1
        news_string += 'NBC:<br>'
        for header in nbc:
            news_string += f'{atag}{header.href}\">{index}. {header.text}</a>'
            news_string += '<br>'
            alternate_string += f'{index}||{header.text}||{header.href}' + '\n'
            index += 1
        news_string += 'FOX:<br>'
        for header in fox:
            news_string += f'{atag}{header.href}\">{index}. {header.text}</a>'
            news_string += '<br>'
            alternate_string += f'{index}||{header.text}||{header.href}' + '\n'
            index += 1
        news_string += 'PROTV:<br>'
        # for header in protv:
        #     news_string += f'{atag}{header.href}\">{index}. {header.text}</a>'
        #     news_string += '<br>'
        #     alternate_string += f'{index}||{header.text}||{header.href}' + '\n'
        #     index += 1
        # news_string += 'DIGI24:<br>'
        # for header in digi24:
        #     news_string += f'{atag}{header.href}\">{index}. {header.text}</a>'
        #     news_string += '<br>'
        #     alternate_string += f'{index}||{header.text}||{header.href}' + '\n'
        #     index += 1
        self.alt_text = alternate_string
        return news_string

    def __str__(self):
        return "News App Main Window Object"

    def __repr__(self):
        return f'MainWindow Object id={id(self)}'


def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
