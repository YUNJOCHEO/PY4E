import random


def guess_numbers():
    n = 3
    numbers = []
    while n > 0:
        number = random.randint(0, 100)
        if number in numbers:
            continue
        else:
            numbers.append(number)
            n = n - 1

    numbers.sort()

    n = 1
    answer = 3
    my_numbers = []
    while answer > 0:
        print(f"{n}차 시도")
        my_number = int(input("숫자를 예측해보세요 : "))
        if my_number not in my_numbers:
            my_numbers.append(my_number)
        else:
            print("이미 예측에 사용한 숫자입니다")
            continue

        if my_number not in numbers:
            print(f"{my_number}는 없습니다")
            if n == 5:
                if my_number > numbers[0]:
                    print(f"최솟값은 {my_number}보다 작습니다")
                else:
                    print(f"최솟값은 {my_number}보다 큽니다")
            if n == 10:
                if my_number > numbers[2]:
                    print(f"최댓값은 {my_number}보다 작습니다")
                else:
                    print(f"최댓값은 {my_number}보다 큽니다")
            n = n + 1
            continue
        else:
            for i in range(len(numbers)):
                if numbers[i] == my_number and i == 0:
                    print(f"숫자를 맞추셨습니다! {my_number}는 최솟값입니다.")
                    n = n + 1
                    break
                elif numbers[i] == my_number and i == 1:
                    print(f"숫자를 맞추셨습니다! {my_number}는 중간값입니다.")
                    n = n + 1
                    break
                else:
                    print(f"숫자를 맞추셨습니다! {my_number}는 최댓값입니다.")
                    n = n + 1
                    break
        answer = answer - 1
    print("게임종료")
    print(f"{n - 1}번 시도만에 예측 성공")
guess_numbers()