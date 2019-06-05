# 표준정의 모듈
from xml.etree.ElementTree import parse
import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import font
import urllib.request
import urllib.parse
import folium
# 사용자정의 모듈
import pharmacyCount

# 메인 클래스
class Pharmacy:
      # 초기화 함수들
      def __init__(self):
            self.window = Tk()
            self.window.geometry("800x500")
            self.window.title("전국약국정보")
            #self.background = PhotoImage(file="resource/background.png")
            #self.bgLabel = Label(image=self.background)
            #self.bgLabel.place(x=0, y=0)

            self.initVariable()
            self.setXML()
            self.initInterface()

            self.window.mainloop()
      def initTextBox(self):
            self.scrollbar = Scrollbar(self.window)
            self.scrollbar.pack()
            self.scrollbar.place(x=785, y=0)

            self.font = font.Font(self.window, size=10, family="Consolas")
            self.renderText = Text(self.window, width=70, height=32, borderwidth=12, relief="ridge", yscrollcommand=self.scrollbar.set)
            self.renderText.pack()
            self.renderText.place(x=268, y=3)
            self.scrollbar.config(command=self.renderText.yview)
            self.scrollbar.pack(side=RIGHT, fill=BOTH)
            self.renderText.configure(state="disabled")
      def initVariable(self):
            self.page = 1
            self.name = ""
            self.area = ""
            self.latitude = 0.0
            self.longitude = 0.0
            self.onText = FALSE
            self.areaCount = pharmacyCount.PharmacyCount()
      def initInterface(self):
            self.initTextBox()
            self.printAllButton()
            self.nextButton()
            self.previousButton()
            self.searchNameLabel()
            self.searchNameButton()
            self.searchAreaLabel()
            self.searchAreaButton()
            self.refreshButton()
            self.renderRoundGraphButton()
            self.renderStickGraphButton()
            self.searchLatLabel()
            self.searchLonLabel()
            self.searchMapButton()

      # 버튼 함수들
      def printAllButton(self):
            self.tempFont = font.Font(self.window, size=12, weight='bold', family='Consolas')
            self.printAllButton = Button(self.window, font=self.tempFont, borderwidth=10, text="전체 출력", command=self.setAll)
            self.printAllButton.pack()
            self.printAllButton.place(x=80, y=20)
      def nextButton(self):
            self.tempFont = font.Font(self.window, size=12, weight='bold', family='Consolas')
            self.nextButton = Button(self.window, font=self.tempFont, borderwidth=10, text=">", command=self.setNext)
            self.nextButton.pack()
            self.nextButton.place(x=745, y=445)
      def previousButton(self):
            self.tempFont = font.Font(self.window, size=12, weight='bold', family='Consolas')
            self.previousButton = Button(self.window, font=self.tempFont, borderwidth=10, text="<", command=self.setPrevious)
            self.previousButton.pack()
            self.previousButton.place(x=265, y=445)
      def searchNameButton(self):
            self.tempFont = font.Font(self.window, size=12, weight='bold', family='Consolas')
            self.searchNameButton = Button(self.window, font=self.tempFont, borderwidth=10, text="이름 검색", command=self.setName)
            self.searchNameButton.pack()
            self.searchNameButton.place(x=155, y=80)
      def searchAreaButton(self):
            self.tempFont = font.Font(self.window, size=12, weight='bold', family='Consolas')
            self.searchAreaButton = Button(self.window, font=self.tempFont, borderwidth=10, text="지역 검색", command=self.setArea)
            self.searchAreaButton.pack()
            self.searchAreaButton.place(x=155, y=140)
      def refreshButton(self):
            self.tempFont = font.Font(self.window, size=12, weight='bold', family='Consolas')
            self.refreshButton = Button(self.window, font=self.tempFont, borderwidth=10, text="갱신", command=self.setXML)
            self.refreshButton.pack()
            self.refreshButton.place(x=500, y=445)
      def renderRoundGraphButton(self):
            self.tempFont = font.Font(self.window, size=12, weight='bold', family='Consolas')
            self.renderRoundGraphButton = Button(self.window, font=self.tempFont, borderwidth=10, text="지역별 분포도(비율)", command=self.areaCount.renderRoundGraph)
            self.renderRoundGraphButton.pack()
            self.renderRoundGraphButton.place(x=42, y=220)
      def renderStickGraphButton(self):
            self.tempFont = font.Font(self.window, size=12, weight='bold', family='Consolas')
            self.renderStickGraphButton = Button(self.window, font=self.tempFont, borderwidth=10, text="지역별 분포도(개수)", command=self.areaCount.renderStickGraph)
            self.renderStickGraphButton.pack()
            self.renderStickGraphButton.place(x=42, y=280)
      def searchMapButton(self):
            self.tempFont = font.Font(self.window, size=12, weight='bold', family='Consolas')
            self.searchMapButton = Button(self.window, font=self.tempFont, borderwidth=10, text="지도검색",
                                                 command=self.setMap)
            self.searchMapButton.pack()
            self.searchMapButton.place(x=175, y=360)

      # 라벨 함수들
      def searchNameLabel(self):
            self.tempFont = font.Font(self.window, size=15, weight="bold", family="Consolas")
            self.nameEntry = StringVar()
            self.inputLabel = Entry(self.window, textvariable=self.nameEntry, font=self.tempFont, width=10, borderwidth=12, relief='ridge')
            self.inputLabel.pack()
            self.inputLabel.place(x=5, y=80)
      def searchAreaLabel(self):
            self.tempFont = font.Font(self.window, size=15, weight="bold", family="Consolas")
            self.areaEntry = StringVar()
            self.inputLabel = Entry(self.window, textvariable=self.areaEntry, font=self.tempFont, width=10, borderwidth=12, relief='ridge')
            self.inputLabel.pack()
            self.inputLabel.place(x=5, y=140)
      def searchLatLabel(self):
            self.tempFont = font.Font(self.window, size=15, weight="bold", family="Consolas")
            self.latEntry = DoubleVar()
            self.inputLabel = Entry(self.window, textvariable=self.latEntry, font=self.tempFont, width=5,
                                    borderwidth=12, relief='ridge')
            self.inputLabel.pack()
            self.inputLabel.place(x=5, y=360)
      def searchLonLabel(self):
            self.tempFont = font.Font(self.window, size=15, weight="bold", family="Consolas")
            self.lonEntry = DoubleVar()
            self.inputLabel = Entry(self.window, textvariable=self.lonEntry, font=self.tempFont, width=5,
                                    borderwidth=12, relief='ridge')
            self.inputLabel.pack()
            self.inputLabel.place(x=90, y=360)

      # 값을 지정하는 함수들
      def setXML(self):
            self.url = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?serviceKey=4hIfjIyALujUTwR1GEnSuiqdWBDt5M1o6Jf5bsAUIdlQQbCeGgmnoYPxgNdj%2FZ0VMw0KSMypf9En7bh12OWhqg%3D%3D" \
                       + "&Q0=" + urllib.parse.quote_plus(self.area) + "&QN=" + urllib.parse.quote_plus(self.name) + "&pageNo=" + str(self.page) + "&numOfRows=10"
            self.tree = ET.ElementTree(file=urllib.request.urlopen(self.url))
            self.tree.write("Data.xml", encoding="utf-8")
            self.data = self.tree.getroot()

            self.doc = parse("Data.xml")
            self.root = self.doc.getroot()
      def setAll(self):
            self.page = 1
            self.name = ""
            self.area = ""
            self.setXML()
            self.printAll()
      def setNext(self):
            if self.onText:
                  self.page += 1
                  self.setXML()
                  self.printAll()
      def setPrevious(self):
            if self.page > 1 and self.onText:
                  self.page -= 1
                  self.setXML()
                  self.printAll()
      def setName(self):
            self.page = 1
            self.name = self.nameEntry.get()
            self.area = ""
            self.setXML()
            self.printAll()
      def setArea(self):
            self.page = 1
            self.name = ""
            self.area = self.areaEntry.get()
            self.setXML()
            self.printAll()
      def setMap(self):
            self.latitude = self.latEntry.get()
            self.longitude = self.lonEntry.get()
            map_osm = folium.Map(location=[self.latitude, self.longitude], zoom_start=13)
            folium.Marker([self.latitude, self.longitude], popup='Mt. Hood Meadows').add_to(map_osm)
            map_osm.save('map.html')

      # 출력함수
      def printAll(self):
            self.onText = TRUE
            self.renderText.configure(state="normal")
            self.renderText.delete(0.0, END)
            for item in self.root.iter("item"):
                  self.renderText.insert(INSERT, "[", INSERT, item.findtext("dutyName"), INSERT, "]", INSERT,
                                         item.findtext("dutyAddr"))
                  self.renderText.insert(INSERT, chr(10))
                  self.renderText.insert(INSERT, "연락처: ", INSERT, item.findtext("dutyTel1"))
                  self.renderText.insert(INSERT, chr(10))
                  self.renderText.insert(INSERT, "월: ", INSERT, item.findtext("dutyTime1s"), INSERT, " ~ ", INSERT,
                                         item.findtext("dutyTime1c"))
                  self.renderText.insert(INSERT, chr(10))
                  self.renderText.insert(INSERT, "화: ", INSERT, item.findtext("dutyTime2s"), INSERT, " ~ ", INSERT,
                                         item.findtext("dutyTime2c"))
                  self.renderText.insert(INSERT, chr(10))
                  self.renderText.insert(INSERT, "수: ", INSERT, item.findtext("dutyTime3s"), INSERT, " ~ ", INSERT,
                                         item.findtext("dutyTime3c"))
                  self.renderText.insert(INSERT, chr(10))
                  self.renderText.insert(INSERT, "목: ", INSERT, item.findtext("dutyTime4s"), INSERT, " ~ ", INSERT,
                                         item.findtext("dutyTime4c"))
                  self.renderText.insert(INSERT, chr(10))
                  self.renderText.insert(INSERT, "금: ", INSERT, item.findtext("dutyTime5s"), INSERT, " ~ ", INSERT,
                                         item.findtext("dutyTime5c"))
                  self.renderText.insert(INSERT, chr(10))
                  self.renderText.insert(INSERT, "토: ", INSERT, item.findtext("dutyTime6s"), INSERT, " ~ ", INSERT,
                                         item.findtext("dutyTime6c"))
                  self.renderText.insert(INSERT, chr(10))
                  self.renderText.insert(INSERT, "일: ", INSERT, item.findtext("dutyTime7s"), INSERT, " ~ ", INSERT,
                                         item.findtext("dutyTime7c"))
                  self.renderText.insert(INSERT, chr(10))
                  self.renderText.insert(INSERT, "위도: ", INSERT, item.findtext("wgs84Lat"), INSERT, chr(10), INSERT, "경도: ", INSERT,
                                         item.findtext("wgs84Lon"))
                  self.renderText.insert(INSERT, chr(10), INSERT, chr(10))
            self.renderText.configure(state="disabled")


Pharmacy()