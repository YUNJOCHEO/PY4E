def good_custom(info):
    info = info.split(',') # , 분리
    #customer = dict() # 고객 정보 담을 dict 생성

    #각 리스트 생성 후 dict에 추가
    id_list = list() #아이디 리스트 생성
    for i in range(len(info)):
        if i % 6 == 0 :
            id_list.append(info[i])

    age_list = list() #나이 리스트 생성
    for i in range(len(info)) :
        if i % 6 == 1 :
            age_list.append(info[i])

    phone_list = list() #전화번호 리스트 생성
    for i in range(len(info)) :
        if i % 6 == 2 :
            phone_list.append(info[i])

    sex_list = list() #성별 리스트 생성
    for i in range(len(info)) :
        if i % 6 == 3 :
            sex_list.append(info[i])

    region_list = list()
    for i in range(len(info)) :
        if i % 6 == 4 :
            region_list.append(info[i])

    num_buy_list = list()
    for i in range(len(info)) :
        if i % 6 == 5 :
            num_buy_list.append(int(info[i]))
    #생성한 리스트를 dict에 추가
    customer_dict = {'아이디' : id_list, '나이' : age_list, '전화번호': phone_list, '성별': sex_list,'지역' : region_list, '구매횟수' : num_buy_list}

    ##여기서부터 모범답안 참고###
    index = list() #전화번호가 없는 회원의 인덱스 저장
    buy = list() #구매횟수가 8회 이상인 회원 인덱스 저장
    for i in range(len(customer_dict['전화번호'])):
        if customer_dict['전화번호'][i] == 'x' :
            index.append(i)
            customer_dict['전화번호'][i] = '000-0000-0000'
        if customer_dict['구매횟수'][i] >= 8:
            buy.append(i)

    #구매횟수가 8회 넘는 회원 중에 전화번호가 있는 회원 인덱스 저장
    true_index = list()
    for i in buy:
        if i not in index:
            true_index.append(i)
    customer_list = list(customer_dict.items())

    #정보 출력
    print(customer_dict)
    for i in true_index:
        print(f"할인 쿠폰을 받을 회원 정보 아이디:{customer_list[0][1][i]}, 나이:{customer_list[1][1][i]}, 전화번호:{customer_list[2][1][i]}, 성별:{customer_list[3][1][i]}, 지역:{customer_list[4][1][i]}, 구매횟수:{customer_list[5][1][i]} ")


good_custom("abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10")