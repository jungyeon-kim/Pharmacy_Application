# 표준정의 모듈
from xml.etree.ElementTree import parse
import xml.etree.ElementTree as ET
import urllib.request
import urllib.parse
import matplotlib.pyplot as plt
import numpy as np

# 그래프를 담당하는 클래스
class PharmacyCount:
    def __init__(self):
        self.tmp = 0
        self.seoulCount = self.getCount("서울특별시")
        self.gyeongGiCount = self.getCount("경기도")
        self.busanCount = self.getCount("부산광역시")
        self.gyeongNamCount = self.getCount("경상남도")
        self.daeguCount = self.getCount("대구광역시")
        self.incheonCount = self.getCount("인천광역시")
        self.gyeongBukCount = self.getCount("경상북도")
        self.chungNamCount = self.getCount("충청남도")
        self.jeonBukCount = self.getCount("전라북도")
        self.jeonNamCount = self.getCount("전라남도")
        self.daejeonCount = self.getCount("대전광역시")
        self.gwangjuCount = self.getCount("광주광역시")
        self.gangWonCount = self.getCount("강원도")
        self.chungBukCount = self.getCount("충청북도")
        self.ulsanCount = self.getCount("울산광역시")
        self.jejuCount = self.getCount("제주특별자치도")
        self.sejongCount = self.getCount("세종특별자치시")

        self.member = ['Seoul', 'GyeongGi', 'Busan', 'Gyeongam', 'Daegu', 'Incheon', 'Gyeongbuk', 'Chungnam', 'Jeonbuk',
                       'Jeonnam', 'Daejeon', 'Gwangju', 'Gangwon ', 'Chungbuk', 'Ulsan', 'Jeju', 'Sejong']
        self.count = [self.seoulCount, self.gyeongGiCount, self.busanCount, self.gyeongNamCount, self.daeguCount,
                      self.incheonCount, self.gyeongBukCount, self.chungNamCount, self.jeonBukCount,
                      self.jeonNamCount, self.daejeonCount, self.gwangjuCount, self.gangWonCount, self.chungBukCount,
                      self.ulsanCount, self.jejuCount, self.sejongCount]
        self.member.reverse()
        self.count.reverse()

    def setXML(self, area):
        self.url = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?serviceKey=4hIfjIyALujUTwR1GEnSuiqdWBDt5M1o6Jf5bsAUIdlQQbCeGgmnoYPxgNdj%2FZ0VMw0KSMypf9En7bh12OWhqg%3D%3D" \
                   + "&Q0=" + urllib.parse.quote_plus(area) + "&pageNo=1&numOfRows=10"
        self.tree = ET.ElementTree(file=urllib.request.urlopen(self.url))
        self.tree.write("Data.xml", encoding="utf-8")
        self.data = self.tree.getroot()

        self.doc = parse("Data.xml")
        self.root = self.doc.getroot()

    def renderRoundGraph(self):
        plt.pie(self.count,
                labels=self.member,
                shadow=False,
                explode=(0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                startangle=90,
                autopct='%1.1f%%')
        plt.title('National Pharmacy Distribution Plot')
        plt.show()
    def renderStickGraph(self):
        plt.bar(self.member, self.count)

        plt.title('National Pharmacy Distribution Plot')
        plt.show()

    def getCount(self, area):
        self.setXML(area)
        for body in self.root.iter("body"):
            self.tmp = body.findtext("totalCount")
            return self.tmp