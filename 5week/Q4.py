from datetime import datetime, timedelta, date

def printDayOfTheWeek (year, month, day):
    dayOfTheWeek = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    return dayOfTheWeek[date(year, month, day).weekday()]

characters = "00:00:00"
myYear = int(input("연도를 입력하시오 : "))
myMonth = int(input("달을 입력하시오 : "))
myDay = int(input("일을 입력하시오 : "))
time1 = datetime(myYear, myMonth, myDay)
myYear, myMonth, myDay= str(time1 + timedelta(days=99)).replace("00:00:00","").strip().split("-")
myDay = int(myDay)
myYear = int(myYear)
myDay = int(myDay)
print(type(myDay))
print(f"{myYear}{myMonth}{myDay}")

print("%d년 %d월 %d일은 %s 입니다." % (myYear, myMonth, myDay, printDayOfTheWeek(myYear, myMonth, myDay)))

#왜 오류가 나는지 모르겠습니다