def baskin31_game():
    import random
    print('<베스킨라빈스31 게임을 시작합니다> \n 나부터 시작!')
    number = 0

    while True:
        #my turn
        my = input('내 차례 - 숫자를 입력해 주세요: ')
        my = my.split()
        #오류 발생 1 : 숫자가 3개 초과하거나 다음 숫자부터 시작하지 않을 때
        if len(my) > 3 or int(my[0]) != number + 1 :
            print('숫자를 제대로 입력해 주세요')
            continue
        #오류 발생 2 : 숫자 2개 입력 시 연속된 숫자가 아닐 경우
        if len(my) == 2:
            if int(my[1]) - int(my[0]) != 1 :
                print('연속된 숫자가 아닙니다!')
                continue
        # 오류 발생 3 : 숫자 3개 입력 시 연속된 숫자가 아닐 경우
        if len(my) == 3:
            if int(my[1]) - int(my[0]) != 1 or int(my[2]) - int(my[1]) != 1 :
                print('연속된 숫자가 아닙니다!')
                continue
        number = int(my[-1])
        print(f"##현재 숫자 : {number}##")
        if number >= 31:
            print('당신이 졌습니다')
            break

        # computer turn
        computer = []
        computer_turn_num = random.randint(1,3)
        for i in range(computer_turn_num):
            number = number + 1
            if number > 31 :
                number = number - 1
                continue
            computer.append(number)
            print(f"컴퓨터 : {computer[-1]}")
        print(f"##현재 숫자 : {number}##")
        if number >= 31:
            print('당신이 이겼습니다')
            break
    print('게임 끝!')

baskin31_game()