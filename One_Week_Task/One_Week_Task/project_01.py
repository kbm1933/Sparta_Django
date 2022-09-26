import random

lotto = set()  # lotto 변수를 set 자료형으로 선언


def get_lotto_number(count):
    result = []
    if count < 1:
        print("1 이상의 값을 입력해주세요")

    for _ in range(count):  # count만큼 반복해서 실행
        lotto = set()

        while len(lotto) < 6:  # lotto의 요소 갯수가 8 이하일 경우 계속해서 반복
            lotto.add(random.randint(1, 9))  # lotto에 1~45 사이의 랜덤 값을 입력

        result.append(lotto)

    return result


lotto_numbers = get_lotto_number(10)
print(lotto_numbers)