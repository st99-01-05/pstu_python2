from data import Data
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        root.title("WebDataAnalyze")
        #setting window size
        width=587
        height=250
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.GListBox_315=tk.Listbox(root)
        self.GListBox_315["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GListBox_315["font"] = ft
        self.GListBox_315["fg"] = "#333333"
        self.GListBox_315["justify"] = "left"
        self.GListBox_315.place(x=20,y=120,width=305,height=94)

        GLabel_209=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_209["font"] = ft
        GLabel_209["fg"] = "#333333"
        GLabel_209["justify"] = "left"
        GLabel_209["text"] = "URLs:"
        GLabel_209.place(x=20,y=90,width=70,height=25)

        self.GLineEdit_270=tk.Entry(root)
        self.GLineEdit_270["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_270["font"] = ft
        self.GLineEdit_270["fg"] = "#333333"
        self.GLineEdit_270["justify"] = "center"
        self.GLineEdit_270["text"] = "Entry"
        self.GLineEdit_270.place(x=20,y=30,width=460,height=54)

        GButton_562=tk.Button(root)
        GButton_562["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times',size=10)
        GButton_562["font"] = ft
        GButton_562["fg"] = "#000000"
        GButton_562["justify"] = "center"
        GButton_562["text"] = "Request"
        GButton_562.place(x=500,y=30,width=72,height=53)
        GButton_562["command"] = self.GButton_562_command

        GLabel_507=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_507["font"] = ft
        GLabel_507["fg"] = "#333333"
        GLabel_507["justify"] = "left"
        GLabel_507["text"] = "Enter Request:"
        GLabel_507.place(x=20,y=0,width=94,height=30)

        self.GListBox_610=tk.Listbox(root)
        self.GListBox_610["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GListBox_610["font"] = ft
        self.GListBox_610["fg"] = "#333333"
        self.GListBox_610["justify"] = "left"
        self.GListBox_610.place(x=340,y=120,width=235,height=92)

        GLabel_183=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_183["font"] = ft
        GLabel_183["fg"] = "#333333"
        GLabel_183["justify"] = "left"
        GLabel_183["text"] = "Sentiment:"
        GLabel_183.place(x=340,y=90,width=70,height=25)

        self.GLabel_486=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_486["font"] = ft
        self.GLabel_486["fg"] = "#333333"
        self.GLabel_486["justify"] = "left"
        self.GLabel_486["text"] = "Status: Enter request"
        self.GLabel_486.place(x=20,y=220,width=300,height=25)

        self.root=root

    def GButton_562_command(self):
        query=self.GLineEdit_270.get()
        self.GLabel_486["text"] = "Status: In process..."
        self.analyzeWeb(query)

    def analyzeWeb(self, query, count=5):
        data = Data()

        list_urls = data.getURLs(query, count)
        nested_URLs = []
        m_url = ""
        for main_url in list_urls:
            html = data.getHTML(main_url)
            nested_URLs = data.getNestedLinks(html)
            m_url = main_url
            if (len(nested_URLs) > 10):
                break

        print(m_url)
        print("URLs nested_links:")
        i=0
        for url in nested_URLs:
            i=i+1
            self.GListBox_315.insert(END,str(i)+") "+url)
            print(url)
        self.root.update()

        maxWordsFrequency = []
        data.initTranslator()
        i=0
        for url in nested_URLs:
            i=i+1
            # Получение_веб_стрнички
            html = data.getHTML(url)
            if (len(html) < 20):
                continue

            # Парсинг_и_перевод
            data.initSoup(html)
            text = data.getTextSoup()
            # translation = data.getTranslate(text)

            # Анализ
            data.initTextBlob(text)
            sentiment = data.getSentiment()
            self.GListBox_610.insert(END,str(i)+") "+f"{sentiment.polarity:.3f}"+"  "+f"{sentiment.subjectivity:.3f}")
            self.root.update()

            self.maxWordsFrequency = maxWordsFrequency+data.getMaxFrequencyWords(1)
            data.listS.append(sentiment.subjectivity)
            data.listP.append(sentiment.polarity)
            data.listI.append(sentiment.polarity * (1 - sentiment.subjectivity))

            print("Веб-страница: ", url)
            print("Слова: ", maxWordsFrequency)
            print("Сентимент: ", sentiment, "\n")

        data.getVizualizeGraphics()
        data.getVizulizeHistogram(self.maxWordsFrequency)

    def analyzeFile(self):
        data = Data()
        data.initTranslator()

        print("Path file for analyze:")

        with open("Data.txt", 'r', encoding='utf8') as file:
            content = file.read().replace('\n', ' ')

        # Перевод
        translation = data.getTranslate(content)

        # Анализ
        data.initTextBlob(translation.text)
        sentiment = data.getSentiment()
        maxWordsFrequency = data.getMaxFrequencyWords(10)

        print("Слова: ", maxWordsFrequency)
        print("Сентимент: ", sentiment, "\n")

        maxWordsFrequency = data.getMaxFrequencyWords(10)
        data.getVizulizeHistogram(maxWordsFrequency, "Text")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
