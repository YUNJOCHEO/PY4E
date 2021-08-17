from datetime import datetime, timedelta, date
characters = "00:00:00"
myYear = int(input("연도를 입력하시오 : "))
myMonth = int(input("달을 입력하시오 : "))
myDay = int(input("일을 입력하시오 : "))
time1 = datetime(myYear, myMonth, myDay)
time1 = str(time1 + timedelta(days=99)).split("-")
time1 = time1.remove("00:00:00")
print(time1)
def printDayOfTheWeek (year, month, day):
    dayOfTheWeek = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    return dayOfTheWeek[date(year, month, day).weekday()]
print("%d년 %d월 %d일은 %s 입니다." % (myYear, myMonth, myDay, printDayOfTheWeek(myYear, myMonth, myDay)))