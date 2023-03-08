import application
from application import FancyWrite, NewsMixin, News, Header, Bbc, Nbc, Fox, Protv, Digi24, MainWindow

# Example headers for Header class
header1 = Header("Example news 1", "Example link 1")
print(str(header1))
print(repr(header1))
print(len(header1))

header2 = Header("Example news 2", "Example link 2")

header3 = Header("Example news 3", "Example link 3", "Example bonus attribute")
print(str(header3))
print(repr(header3))
print(len(header3))
print(header3[2])


# Example news object for News class
news_object = News()
print(str(news_object))
print(repr(news_object))

# Example of operator overloading
news_object += header1
news_object += header2
news_object += header3
print(str(news_object))
print(repr(news_object))
print(len(news_object))
news_object[1] = news_object[2]
del news_object[2]
print(news_object)
print(len(news_object))

# The News objects are iterable
for header in news_object:
    print(header.text)

# Example of classes for each news source. They all inherit from news
# get_first_x_news() method comes from the NewsMixin mixin
bbc = Bbc()
bbc = bbc.get_first_x_news(4)
print(str(bbc))
print(repr(bbc))

nbc = Nbc()
nbc = nbc.get_first_x_news(2)
print(str(nbc))
print(repr(nbc))

# fox = Fox()
# fox = fox.get_first_x_news(1)
# print(str(fox))
# print(repr(fox))

# protv = Protv()
# protv = protv.get_first_x_news(1)
# print(str(protv))
# print(repr(protv))

# digi24 = Digi24()
# digi24 = digi24.get_first_x_news(1)
# print(str(digi24))
# print(repr(digi24))

# Example of get_news() generator implemented for each source class
# This is the same as the get_first_x_news() method
bbc_news_generator = Bbc.get_news()
for i in range(3):
    print(next(bbc_news_generator))

nbc_news_generator = Nbc.get_news()
for i in range(2):
    print(next(nbc_news_generator))

# All the news sources classes have a method to get all of today's headers for later searching
all_bbc_news = Bbc.get_all_news()
# print(str(all_bbc_news))
# print(repr(all_bbc_news))

all_nbc_news = Nbc.get_all_news()
# print(str(all_nbc_news))
# print(repr(all_nbc_news))

# all_fox_news = Fox.get_all_news()
# print(str(all_fox_news))
# print(repr(all_fox_news))

# all_protv_news = Protv.get_all_news()
# print(str(all_protv_news))
# print(repr(all_protv_news))

# all_digi24_news = Digi24.get_all_news()
# print(str(all_digi24_news))
# print(repr(all_digi24_news))

# Example of Context Manager Usage:
# FancyWrite writes titles and links to a file named dd-mm-yyyy_articles.txt
with FancyWrite() as fwrite:
    fwrite.fancy_write("Example title", "Example link")

# Uncomment the next line to initialize the GUI Window
# application.window()
