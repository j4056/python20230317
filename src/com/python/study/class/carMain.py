'''
.... 클래스명: car
인스턴스 변수
........company
........model
........color
....인스턴스 메소드
........carInfo()
........회사명: 현대자동차
........모델명: 펠리세이드
........색상: 화이트
'''

class car
....def __init__(self,company, model, color):
........self.company = company
........self.model = moodel
........self.color = color

....def carInfo(self):


.........return f'''회사명: 
회사명: {self.company}
모델명: {self.model}
색상: {self.color}
''')

form src.com.python.study.classstudy.car import car

if __name__ ' __main__':
carList = List()

c1 = car('현대자동차', '펠리세이드', '화이트')
c2 = car('현대자동차', '쏘나타', '블랙')

....print(c1)
carList.append(c1)
carlist.append(c2)

....for car0bj in carList:
........print(car0bj)
........print(f'회사명: {car0bj.model}')


