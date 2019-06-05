# 표준정의 모듈
import folium


# 그래프를 담당하는 클래스
class PharmacyMap:
    def __init__(self):
        self.latitude = 0.0
        self.longitude = 0.0
    def makeMap(self, latitude, longitude):
        print(latitude)
        map_osm = folium.Map(location=[latitude, longitude], zoom_start=13)
        folium.Marker([latitude, longitude], popup='Mt. Hood Meadows').add_to(map_osm)
        map_osm.save('map.html')