"""
자료구조

시퀀스
요소로 구성
요소간에 순서 있음
시퀀스의 요소들은 번호가 붙여져 있음
내장 시퀀스(str, bytes, bytearray, list, tuple, range)
동일한 연산을 지원
인덱싱, 슬라이싱, 덧셈연산, 곱셈연산

튜플

t = ("김회창",) // 원소가 하나밖에 없을 땐 마지막에 쉼표를 넣어줘야 튜플로 인정된다.
t = "apple", "banana", "grape" // 괄호가 없더라도 튜플로 인정되는 경우
튜플 내 원소는 변경이 불가능하다.

튜플끼리 더하기 가능, 리스트에 튜플더하기 가능

n1 = 90
n2 = 10

n1, n2 = (n2, n1) // 튜플을 사용하여 두 원소의 값을 바꿀 수 있음
딕셔너리에서 키로 사용할 수 있음 <-> 리스트는 불가!

세트

집합 연산이 가능하다.

부분집합 : setA.issubset(setB)가 true 일 경우는 집합 A가 B의 부분집합임을 의미
합집합 : set.union, A | B
교집합 : set.intersection, A & B
차집합 : set.difference, A - B

clear를 통해 모든 원소 제거가능
discard와 remove를 통해 원소 제거 가능
discard 는 제거하려는 원소가 없더라도 error를 일으키지 않는다.

딕셔너리

집합연산 가능하다.
key : value로 이루어진 쌍

capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"}

t = capitals.get("France","해당 키가 없습니다.")
위의 상황에서 get을 통해 해당 key에 해당하는 value값을 찾으려 할 때
key값 자체가 존재하지 않을 경우를 대비해 두 번째 인자로 없을 경우 반환값을 넣는다.

모든 값을 제거하는 건 없다.

문자열
문자열도 크게 보면 시퀀스라는 자료구조에 속한다.
chr() : 정수를 문자로 변환
ord() : 문자를 정수로 변환 (아스키 값)
문자열의 원소를 인덱스로 접근하여 값을 바꿀수 없다. (불변 객체)

문자열 뒤에 어떤 문자가 존재하는지 검사
string.endswith("")

객체와 클래스

객체지향 프로그래밍에서는 서로 관련 있는 데이터와 함수를 묶어서 객체로 만들고 이들 객체들이 모여서 하나의 프로그램이 된다.

절차지향 프로그래밍은 프로그램 내부 실행순서를 기반으로 하는 프로그래밍 방법이고
객체지향 프로그래밍은 데이터와 함수를 하나의 덩어리로 묶어서 생각하는 방법이다.

캡슐화 : 공용 인터페이스만 제공하고 구현 세부 사항을 감추는 것

class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count+=1
a = Counter()
a.increment()
print(a.count)

class TV:
    serialNumber = 0 // 클래스 변수

    def __init__(self, channel, volume, on): // 생성자 정의
        self.__channel = channel // 정보은닉
        self.volume = volume // 인스턴스 변수
        self.on = on
    def show(self):
        print(self.channel, self.volume, self.on)
    def setChannel(self, channel): // setter
        self.__channel = channel
    def getChannel(self): // getter
        return self.__channel


정보은닉

파이썬에서 클래스 인스턴스 변수를 정의 할 때, 다른 클래스나 외부에서 접근을 할 수 없도록 private선언을 할 수 있다.
언더바 두개를 붙이면 된다.

객체 참조

파이썬에서 변수는 실제로 객체를 저장하는 것이 아니다.
객체는 메모리에 띄우고, 그 메모리상에 어디에 위치해 있는지에 대한 주소만을 저장한다

따라서 다른변수가 같은 객체에 대하여 참조하고 있는지 검사하는  is, not is 가 있다.

c = TV()
t = c
if c is t 를 했을 때 통과 할 수 있다.

None = 아무것도 참조하지 않는 값을 정의 할때 사용
c = None

따라서 다른 함수에서 객체를 받아서 처리 할 때 매게변수가 같은 객체를 참조하게 되어
값을 바꿀 수 있게 된다.

클래스 변수 (클래스 멤버)

클래스 내부에서 전역 변수처럼 쓰이는 변수
보통 상수값들을 정의 할 때 쓰인다.

특수 메소드

파이썬에는 연산자에 관련된 특수 메소드가 잇다.
객체에 대한 연산을 적용한다.

파일 입출력

open(파일이름, 파일모드)
파일모드에는 r, w, a, r+ 가 있다.
각각 읽기, 쓰기, 이어쓰기, 읽기+쓰기

한글 인코딩 에러 cp949 error
file= open("경로","파일모드",encoding="UTF-8")

디렉토리
os 라이브러리를 받고

getcwd : 현재 작업중인 디렉토리 객체 반환
chdir : 작업 디렉토리 바꾸기
listdir : 해당 디렉토리 내부 파일 리스트 받기

ex) 작업 디렉토리에서 확장자가 ".jpg"로 끝나는 파일을 모두 찾아서 파일 이름 출력하기

import os

dir =  os.getcwd()
files = dir.listdir()

for names in files:
    if os.path.isfile(names):
        if name.endswith(".jpg"):
            print(name)
이진파일 읽기
파일모드에 rb를 사용한다.

filr = open(filename, "rb")
bytesarray = file.read(8) // 8바이트 읽기

이진파일 쓰기
파일모드에 wb를 사용하며, bytes로 정의된 객체를 write한다.

outfile = open(filename, "wb")
bytesArray = bytes([2,45])
outfile.write(bytesArray)

객체 입출력
pickle 모듈의 dump() load() 메소드를 사용하면
객체를 쓰고 읽을 수 있다.

dump가 저장, load가 불러오기

저장
import pickle
dict = {
    # 내용들
}
file = open("d:\\save.p","rb")
pickle.dump(dict, file)

불러오기
file = open("d:\\save.p", "rb") 이진파일을 읽기
obj = pickle.load(file)
읽어들어온 이진 데이터를 pickle 라이브러리 속 load 메서드를 통해 python 딕셔너리 폼으로 변환

예외처리
try:

except(오류):

ex)
ZeroDivisionError
(x, y) = (2, 0)
try:
    z= x/y
except ZeroDivisionError:
    print("0으로 나누는 예외1")
else:
    print("정상적으로 나누어졌음")
finally:
    print("try블록 통과")

상속 (inheritance)

기존에 존재하는 클래스로부터 코드와 데이터를 이어받고 자신이 필요한 기능을 추가하는 기법이다.

객체지향 프로그래밍에서는 상속이 클래스간에 is-a 관계를 생성하는데 사용된다.

상속 구현하기

class 자식클래스(부모클래스) :
    def __init__(self, ...):
        super.__init__(...) // 부모클래스 생성자로 넘겨줌
    def 메소드1(self, ...):

    def 메소드2(self, ...):


ex) Car 클래스와 Car을 상속받은 ElectricCar
class Car:
    def __init__(self, make, model, color, price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price
    def setMake(self, make):
        self.make= make
    def getMake(self):
        return self.make

    def getDesc(self):
        return "차량 = (" + str(self.make)+","+\str(self.model)+","+\str(self.color)+","+\str(self.price)+")"

class ElectricCar(Car):
    def __init__(self, make, model, color, price, batterySize):
        super().__init__(make, model, color, price)
        self.batterySize = batterySize
    def setBatterySize(self, batterySize):
        self.batterySize =batterySize
    def getBatterySize(self):
        return self.batterySize

파이썬은 다중상속을 지원한다.

class 자식클래스 명(부모 클래스 1, 2)로 다중상속을 지원한다.
다중상속을 받은 자식클래스의 생성자에서는

일반적인 상속을 받은경우 super.__init__()을 통해 알맞은 값만을 넘겨주지만
다중상속인 경우에는 어떤 부모클래스에 어떤 값을 넣어주느냐에 따라 의미가 달라지므로

부모클래스1.__init__(self, ...)
부모클래스2.__init__(self, ...)

위와 같은 방식으로 넘겨준다.

메소드 오버라이딩

부모클래스에 정의된 메소드를 자식클래스에서 재정의 하는것을 의미

다형성(polymorphism) :
하나의 식별자로 다양한 타입을 처리하는 것을 의미한다.

일반적으로 상속과 다형성의 관계에서는

추상 메소드를 상속받은 클래스에서 정의 하여 사용할 때 클래스의 의도에 맞게 정의 하여 사용이 가능하다.

내장함수에서 여러 종류의 인자를 받는 경우도 다형성이라 볼 수 있다.

상속과 다형성

ex) Shape 클래스를 상속받는 도형종류들은 그에 맞는 도형을 draw해야한다.

class Shape:
    def __init__(self, name):
        self.name = name
    def getArea(self):
        raise NotImplementedError("이것은 추상 메소드입니다.")

class Circle(Shape):
    def __init__(self, name, radius):
        self.radius = radius
        super.__init__(name)
    def getArea(self): // 다형성 적용하여 상황에 맞는 기능을 수행한다.
        return 3.141592*self.radius**2
class Rectangle(Shape):
    def __init__(self, name, width, height):
        self.width = width
        self.height = heigth
        super().__init__(name)
    def getArea(self):
        return self.width * self.height


object 클래스

모든 클래스의 맨 위에는 object 클래스가 있다고 생각하면 된다.

클래스 관계에서 is-a 관계는 상속 관계이다.
클래스 관계에서 has-a 관계는 구성 관계이다.


all() : 모든 항목이 참이면 True를 반환한다.
mylist = [1,3,4,5]
all(mylist) : True
mylist = [1,3,4,0]
all(mylist) : False

any() : 시퀀스 객체에 있는 한 개의 항목이라도 참인 경우 참을 반환한다.

dir() : 객체가 가지고 있는 변수나 함수를 보여줌

제너레이터 : 키워드 yield를 사용하여 함수로부터 이터레이터를 생성하는 하나의 방법이다.

def myGenerator():
    yield 'first'
    yield 'second'
    yield 'third'
위의 제너레이터는 이터레이터 객체로서 __next__()를 통해 내부의 값들을 순환할 수 있다.

copy 모듈
shallowcopy() : 얕은 복사
deepcopy() : 깊은복사

keyword 모듈
keyword.iskeyword(name) : 예약어인지 판단해줌
keyword.kwlist : 예약어 리스트를 반환

MatPlot : GNUplot 처럼 그래프를 그리는 라이브러리이다.

import matplotlib.pyplot as plt
plt.plot(리스트)
plt.show()
리스트의 값을 그래프로 나타내는데 이 때 리스트의 인덱스를 x축으로 가지게 된다.
x= 리스트
y = 리스트
plt.plot(x,y)
plt.show()
각각의 리스트를 x축y축으로 가지는 그래프를 형성
plt.xlabel("")
plt.ylabel("")
해당하는 직선 그래프의 x축 y축의 의미를 정의

y1 = 리스트
y2 = 리스트

plt.plot(x,y1,x,y2)
plt.xlabel("day")
plt.ylabel("temperature")
plt.show()
x, y1의 자료와 x, y2의 자료를 갖는 각각의 직선 그래프를 하나의 차트에 표현

plt.plot(x,y1,label=라벨이름)
plt.plot(x,y2,label=라벨이름)

plt.legend(loc="upper left")
plt.title(차트이름)

위와 같은 차트를 나타내는데 각각의 그래프 이름을 label= 으로 정해주고 legend의 loc=을 통해 위치를 정해준다.
title은 차트의 제목이다.

plt.plot(리스트, "sm")
plt.show()

점선 그래프로 표현

plt.bar(x리스트, y리스트)
plt.show()

막대 그래프로 표현

3차원 그래프
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 3차원 축을 얻는다.
axis = plt.axes(projection='3d')

# 3차원 데이터를 넘파이 배열로 생성
Z = np.linspace(0,1,100)
X = Z*np.sin(30*Z)
Y = Z *np.cos(30*Z)

axis.plot3D(X,Y,Z)
plt.show()

넘파이의 기초

넘파이는 행렬 계산을 위한 파이썬 라이브러리 모듈이다.

넘파이 배열로 변환
import numpy as np

ftemp= [63,73,80]

F = np.array(ftemp)

모든 리스트의 원소에 적용시킬 연산이 있다면
그대로 연산식에 numpy 객체를 넣어주면 원소별로 연산이 적용된체 반환된다.

F = (F-32)*5/9
print(F)
array([17.7777777,22.7777778,26.6666667])

넘파이 배열간에 모든 연산자가 사용가능하다.

A = np.array([1,2,3])
B = np.array([1,2,3])

result = A+B
print(result)

array([2,4,6])

a = np.array([1,0,2,3])
a = a>0
print(a)

array([True, False, True, True])

arange : 넘파이의 데이터 생성 함수 (시작, 종료, 간격)

A = np.arange(1,10,2)
print(A)

array([1,3,5,7,9])

linspace : 넘파이의 데이터 생성함수 (시작, 종료, 개수 = 50) # default는 50개이다.

A = np.linspace(0,10,100) : 0~10사이에 100개의 데이터를 리스트로 구성하시오

균일 분포 난수 생성

np.random.seed(100) # 시드설정
np.random.rand(행, 열) # 행만이 설정되면  1차원 리스트, 행과 열 모두 주어지면 2차원 리스트

정규 분포 난수 생성
np.random.randn(행, 열) # 위의 균일분포 난수생성과 동일한 성질을 띔
default로는 평균값이 0이고 표준편차가 1.0인 정규분포 난수가 생성되는데
다른 값을 주려고 한다면

m, sigma= 10,2
m+sigma*np.random.randn(5) 를하게 되면 평균값이 10이고 표준편차가 2.0인 정규분포가 완성된다.

넘파이 내장함수 sin()
a = np.array(리스트)
a = np.sin(a)

axis = 0 : 열
axis = 1 : 행

mean() : 평균
std() : 표준편차
var() : 분산

mean(axis=0) : 열의 평균
mean(axis=1) : 행의 평균


모든 배열의 요소에 sin함수가 적용된다.


히스토그램 그리기
import matplotlib.pylot as plt
import numpy as np

numbers = np.random.normal(size=10000)

plt.hist(numbers)
plt.xlabel("value")
plt.ylabel("freq")
plt.show()

일반적인 인덱싱도 가능하며 논리적인 인덱싱도 가능하다.

ex) numpy배열로 된 age 배열에서 20보다 큰 데이터만 뽑아내라
import numpy as np
age = np.array([18,19,25,30,28])
y = age[age>20]

전치행렬
어떤 행렬이 주어졌을 때 행과 열을 바꾼 행렬을 전치행렬이라 한다.

x= np.array([[1,2,3],[4,5,6],[7,8,9]])
x = x.transpose() 혹은 x = x.T

선형 방정식
방정식을 해결해준다.
3*x0+x1 = 9
x0+2*x1 = 8
위의 방정식을 numpy식 배열로 표현하면

a = np.array([3,1],[1,2])
b = np.array([9,8])
이 되고 이를 해결하기 위해서는 linalg.solve()를 사용한다.
x = np.linalg.solve(a,b)
print(x)
"""
f = open("d:\\input.txt","r",encoding="UTF-8")
line = f.readline().rstrip()
while line !="":
    print(line)
    line = f.readline().rstrip()


class Car:
    def __init__(self, make, model, color, price):
        self.__make = make
        self.model = model
        self.color = color
        self.price = price
    def setMake(self, make):
        self.__make= make
    def getMake(self):
        return self.__make

    def getDesc(self):
        return "차량 = (" + str(self.__make)+","+str(self.model)+","+str(self.color)+","+str(self.price)+")"

class ElectricCar(Car):
    def __init__(self, make, model, color, price, batterySize):
        super().__init__(make, model, color, price)
        self.batterySize = batterySize
    def setBatterySize(self, batterySize):
        self.batterySize =batterySize
    def getBatterySize(self):
        return self.batterySize
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name, self.age)
class Student:
    def __init__(self, id):
        self.id = id
    def getId(self):
        return self.id
class CollegeStudent(Person, Student):
    def __init__(self, name, age, id):
        Person.__init__(self, name, age)
        Student.__init__(self, id)
def main():
    myCar = ElectricCar("Tisla", "ModelS","White",10000,0)
    print(myCar.getDesc()) # 상속을 받고서 부모클래스의 생성자로 넘어간 값에는 batterySize는 없으며, Desc메서드 자체에도 batterySize를 출력하진 않는다.
    myCar.setMake("Tesla")
    myCar.setBatterySize(60)
    print(myCar.getDesc())
    # print(myCar.__make) 부모클래스의 make가 이미 private 선언되어 있으므로 당연히 접근이 안된다.

    # 다중상속을 받은 클래스의 생성자 안에서는
    # 부모 클래스 각각의 생성자를 호출하여 self 와 함께 value 들을 알맞게 넣어야한다.
    obj = CollegeStudent("kim",22,"100036")
    obj.show()
    print(obj.getId())


main()

import numpy as np
# 리스트를 넘파이로 변환
a = np.array([1,2,3,4])
# 넘파이는 모든 연산자 적용 가능
a = a*2
print(a)
b = np.array([1,2,3,4])
a = a-b
print(a)
# arange(시작, 종료, 간격) 넘파이 데이터 생성
p = np.arange(1,11,2)
print(p)
# linspace(시작, 종료, 개수=50)
p = np.linspace(0,10,20)
print(p)
# 균일 분포 난수 생성
np.random.seed(100) # 시드값 설정
b= np.random.rand(2,3) # 균일분포 난수 생성 (행,열)
print(b)
# 정규 분포 default 평균값(m)은 0, 표준편차(sigma)는 1.0
t = np.random.randn(5)
print(t)
# 내가 정한 평균값(m)과 표준편차(sigma)를 적용한 정규 분포 난수를 생성하기 위해서는
# 생성된 난수에 표준편차를 곱하고 평균값을 더하면 된다.
m, sigma = 10,2
t = m+sigma*np.random.randn(5)
print(t)
# 위와 같은 것을 형성하는 np.random.normal(m, sigma, 개수)
t= np.random.normal(m, sigma, 5)
print(t)
# 배열 인덱싱에서 내가 원하는 조건대로 인덱싱하려면
# 배열이름[ 배열이름 조건 ]
age = np.array([18,19,25,30,28])
y = age[age>20] # 20보다 큰 데이터만 age 배열로 재구성 해라
print(y)

# 2차원 배열의 인덱싱
# 배열이름[행기준, 열기준]
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
a= a[0:2,1:3]
print(a)

# 전치행렬 연산하기
# 어떤 2차원 배열.transpose() 혹은 2차원배열.T

x = np.array([[1,2,3],[4,5,6],[7,8,9]])
#x = x.transpose()
x = x.T
print(x)