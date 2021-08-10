def check_id(id_number):
    while True:
        if len(id_number) != 14 or id_number.find("-") == -1:
            print("잘못된 주민등록번호입니다, 다시 입력해주세요..")
            break
        # 21 이하의 숫자로 시작하면 2000년 이후 출생인지 물어보기
        if int(id_number[:2]) <=21:
            q = input("2000년 이후 출생자 입니까? 맞으면 o 아니면 x : ")
            # 2000년 이후 출생일 때
            if q == "o":
                if id_number[7] not in ["3" ,"4"]:
                    print("잘못된 주민등록번호입니다.")
                else:
                    if id_number[7] == "3":
                        gender = "남자"
                    else:
                        gender = "여자"
            # 아닐때 1900년 ~ 1921년 사이 출생일 때
            elif q == "x":
                if id_number[7] == "1":
                    gender = "남자"
                else:
                    gender = "여자"
            else:
                continue
        # 1922년 ~ 1999년 사이 출생일 때
        else:
            if id_number[7] not in ["1" , "2"]:
                print("잘못된 주민등록번호입니다, 다시 입력해주세요.")
            else:
                if id_number[7] == "1":
                    gender = "남자"
                else:
                    gender = "여자"
        year = id_number[:2]
        mon = id_number[2:4]
        try:
            print(f"{year}년{mon}월 {gender}")
        except:
            print("올바른 번호를 넣어주세요")
            break
id_number = str(input('주민등록번호를 넣어주세요.(-도 써 주세요.) :'))
check_id(id_number)

a = "500629-2222222"
check_id(a)