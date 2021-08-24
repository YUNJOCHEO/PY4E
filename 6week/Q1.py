def king_duplicate(korea_king, chosun_king) :
    counts = dict()

    # 고려시대 왕 + 조선시대 왕 하나로 합침
    kings = korea_king + ','+ chosun_king
    # , 로 구분
    kings = kings.split(',')
    # 왕 이름, 횟수로 구성된 딕셔너리 생성
    for king in kings :
        counts[king] = counts.get(king,0) + 1
    # 중복되는 왕 이름의 수 출력
    counts_dupl = 0
    for k,v in counts.items():
        if v >= 2:
            print('조선과 고려에 모두 있는 왕 이름 : ',k,)
            counts_dupl = counts_dupl + 1
    print(f"조선과 고려에 모두 있는 왕 이름은 총 {counts_dupl}개 입니다")

king_duplicate("태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"
               ,"태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종")