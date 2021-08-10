import re
a = re.compile('010-\d{4}-\d{4}')
def wrong_guest_book(guest_book):
    # text 파일 저장
    text_save = open("guest_book.txt", "w")
    text_save.write(guest_book)
    text_save.close()

    # 파일 불러오기
    file = open("guest_book.txt").read().strip()
    for line in file.split("\n"):
        name, num = line.split(",")
        if a.match(num):
            continue
        print(f"잘못 쓴 사람: {name}")
        print(f"잘못 쓴 번호: {num}")
        print()

guest_book = """
김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333
"""
wrong_guest_book(guest_book)