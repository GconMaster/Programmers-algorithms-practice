def Harshad(n):
    # n은 하샤드 수 인가요?
    Sum_n = 0
    for i in str(n):
        Sum_n += int(i)
    if n % Sum_n == 0:
        return True
    else:
        return False

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))