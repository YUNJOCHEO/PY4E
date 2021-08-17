import random
print("베스킨라빈스 31 게임 프로그램입니다!")
#호출되는 숫자 함수
def call_numbers(size, called):
    for _ in range(size):
        called += 1
        print("'{0}'".format(called))
        if called == 31:
            break
    return called
#잘못 호출된 숫자 입력시 재입력 하는 함수
def validate_input(prompt, valid_list):
    while True:
        value = input(prompt)
        if value in valid_list:
            value = int(value)
            break
        else:
            print("잘못된 입력입니다. 재입력해주세요.")
    return value
# 컴퓨터가 호출하는 함수
def call_computer(call_status):
    if call_status % 4 == 0:
        computer_call = 2
    elif call_status % 4 == 1:
        computer_call = 1
    elif call_status% 4 == 3:
        computer_call = 3
    else:
        computer_call = random.randint(1, 3)
    return computer_call
# 누가 먼저 호출할지 결정
order = validate_input("순서를 입력하세요. (선공격 1, 후공격 0 입력) : ", ['0', '1'])
call = 0
count = 1
#사용자는 호출할 숫자의 갯수를 입력함으로써, 게임 진행
while call < 31:
    if count % 2 == order:
        # 사용자의 차례
        print('사용자의 차례')
        size_of_call = validate_input("호출할 개수를 입력하세요 : ", ['1', '2', '3'])
        call = call_numbers(size_of_call, call)
    else:
        # 컴퓨터의 차례
        print('컴퓨터의 차례')
        size_of_call = call_computer(call)
        call = call_numbers(size_of_call, call)
    count += 1
if count % 2 == order:
    print("사용자가 승리하셨습니다!!")
else:
    print("컴퓨터의 승리!!")
#Q3. 숫자맞추기 게임(컴퓨터가 임의의 숫자를 3개 만들고 우리가 맞추는게임)
import random
random_number= []
while len(random_number)<3: # 숫자 3개 무작위 지정
    number = random.randint(0,100) #무작위 숫자 0~100
    if number not in random_number :
        random_number.append(number)
random_number.sort() #리스트 정렬 sort
print(random_number)
answer_count = 0
guess_count = 1
guess_list = []
while answer_count < 3:
    print(f"{guess_count}차 시도")
    answer = int(input("숫자를 예측해보세요 : "))
    if answer in guess_list :
        print("이미 사용된 숫자입니다")
    else:
        guess_list.append(answer)
    if answer in random_number :
        print("숫자를 맞추셨습니다.")
        answer_count = answer_count+1
        if (random_number.index(answer) ==0):
            print(f"{answer}는 최소값입니다.")
        elif (random_number.index(answer) == 1):
            print(f"{answer}는 중간값입니다.")
        elif (random_number.index(answer) == 2):
            print(f"{answer}는 최대값입니다.")
        else:
            print(f"{answer}는 없습니다")
            if guess_count > 5 :
                if random_number[0] <answer:
                    print(f"최소값은 {answer}보다 {answer-random_number[0]} 작습니다.")
                else:
                    print(f"최소값은 {answer}보다 {random_number[0]-answer} 큽니다.")
            elif guess_count > 10 :
                if random_number[2] <answer:
                    print(f"최대값은 {answer}보다 {answer-random_number[2]} 작습니다.")
                else:
                    print(f"최대값은 {answer}보다 {random_number[2]-answer} 큽니다.")
guess_count = guess_count + 1