def grader(student, answers):
    name = []  # 이름을 분리하여 저장할 리스트
    answer = []  # 학생들의 답을 분리하여 저장할 리스트
    scores = []  # 채점후 점수를 저장할 리스트
    for s in student:
        s = s.split(",")  # ,를 기준으로 이름과 정답지로 분리
        name.append(s[0])
        answer.append(s[1])

    score = 0
    # 점수 계산
    # 한 명씩 점수 계산, 답지와 내답이 같으면 10점 추가, 10문제라서 문제당 10점
    for a in answer:
        for i in range(len(a)):
            if int(a[i]) == answers[i]:
                score = score + 10
        scores.append(score)
        score = 0

    # 이름과 점수를 결합
    for i in range(len(name)):
        name[i] = str(scores[i]) + name[i]
    # 점수 기준 내림차순 정렬
    name.sort(reverse=True)

    # 한 사람씩 출력
    for i in range(len(name)):
        print(f"학생: {name[i][2:]} 점수: {name[i][:2]}점 {i + 1}등")


s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]
a = [3,2,4,2,5,2,4,3,1,2]