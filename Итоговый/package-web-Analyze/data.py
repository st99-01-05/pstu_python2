import requests
from googlesearch import search
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from textblob import TextBlob
from googletrans import Translator
from nltk.corpus import stopwords
from textblob.en.sentiments import NaiveBayesAnalyzer
from PIL import Image
import matplotlib.pyplot as plt
import nltk

class Data:
    listP=[]
    listS=[]
    listI=[]

    def initSoup(self, html):
        print("parsing...")
        #Инициализация  парсинга html
        self.soup = BeautifulSoup(html, 'html.parser')

    def initTextBlob(self, text):
        #nltk.download('punkt')
        #nltk.download('movie_reviews')

        print("analyze_text...")
        #Инициализация  и   обработка   текста
        self.textBlob = TextBlob(text,)
        list = [word for word in self.textBlob.words if word not in stopwords.words('english')]
        text = ' '.join(list)
        self.textBlob = TextBlob(text)

    def initTranslator(self):
        #Иницилизаация  переводчика
        self.translator = Translator()

    def getMaxFrequencyWords(self,count):
        #Получение слов
        sorted_dict = sorted(self.textBlob.word_counts.items(), key=lambda x: x[1], reverse=True)
        result=[]
        if(count>len(self.textBlob.word_counts)):
            count=len(self.textBlob.word_counts)
        for i in range(count):
            result.append(sorted_dict[i])
        return result

    def getTranslate(self, text):
        print("translate...")
        # Перевод текста на английский
        return self.translator.translate(text)

    def getSentiment(self):
        #Получение  оценки  текста
        return self.textBlob.sentiment

    def getLinkInHTML(self, html):
        links = []
        res_find = self.soup.find_all('a')

        max_link = 0
        for item in res_find:
            if (max_link > 10):
                break
            arr = str(item.string).split()
            if (len(arr) > 3):
                max_link = max_link + 1
                print(len(arr), item.get('href'), item.get('class'), item.string)

    def getTextSoup(self):
        #Получение  текста  после  парсинга
        return self.soup.get_text()

    def getNestedLinks(self,html,max_nested=70):
        tempSoup=BeautifulSoup(html,'html.parser')
        nested_links=[]
        for a in tempSoup.find_all('a', href=True):
            if (a['href'].count('/')>=4):
                nested_links.append(a['href'])
            max_nested  =   max_nested-1
            if max_nested<=0:
                return nested_links
        return  nested_links
    def getHTML(self,url):
        print("get_html...")
        ua = UserAgent()
        text=""
        try:
            r = requests.get(url, headers={'User-Agent': ua.firefox})
            r.raise_for_status()
            text=r.text
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)
        return text

    def getURLs(self,query, num_results=5):
        list = []
        # Выполняем поиск и выводим результаты
        for result in search(query, num_results=num_results):
            list.append(result)
        return list

    def getVizulizeHistogram(self, list, title):

        # Извлечение слов и количества упоминаний
        words = [word for word, count in list]
        counts = [count for word, count in list]

        # Создание гистограммы с метками оси X
        plt.barh(words, counts)

        # Поворот меток оси X
        plt.xticks(rotation=0)

        # Добавление подписей осей и заголовка
        plt.xlabel('Counts')
        plt.ylabel('Words')
        plt.title(title)
        # Отображение гистограммы
        plt.show()

    def getVizualizeGraphics(self):
        # Создание подграфиков
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)

        # Построение первого графика
        ax1.plot(self.listP)
        ax1.set_ylabel('Polarity')

        # Построение первого графика
        ax2.plot(self.listS)
        ax2.set_ylabel('Subjectivity')

        # Построение второго графика
        ax3.plot(self.listI)
        ax3.set_xlabel('X')
        ax3.set_ylabel('Influence')

        # Отображение графиков
        plt.show()
