import numpy
def sales_management(names, records):
    record_dict = dict()  # 멤버의 실적을 기록할 dict 생성
    # 실적 기록
    for i in range(len(names)):
        record_dict[names[i]] = records[i]
    # 실적을 평균으로 바꿔서 저장
    for (k, v) in record_dict.items():
        mean = numpy.mean(v)
        record_dict[k] = mean
    # 평균 실적이 높은 순서대로 저장
    ranking = [(v, k) for k, v in record_dict.items()]
    ranking = sorted(ranking, reverse=True)

    # 예비 보너스, 면담 대상자 저장
    bonus_names = (ranking[0][1], ranking[1][1])
    counsel_name = (ranking[4][1], ranking[5][1])

    # 5보다 작으면 보너스 대상자 제외
    for bn in bonus_names:
        if record_dict[bn] < 5:
            continue
        print(f"보너스 대상자 {bn}")
    print("-------------------------\n")

    # 3보다 높으면 면담 대상자 제외
    for cn in counsel_name:
        if record_dict[cn] > 3:
            continue
        print(f"면담 대상자 {cn} ")

# 이름, 실적
member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2],
           [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
           [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]
sales_management(member_names, member_records)