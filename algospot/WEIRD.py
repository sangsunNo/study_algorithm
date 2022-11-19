import sys


def solve(leng, summ, target):  # 부분합 중 수 자체와 같은 것이 있는지 검사
    if summ == target:  # leng=약수집합의 길이, summ=약수의 부분합, target=검사하는 수 자체
        return True
    if summ < target or target < 0:
        return False
    if solve(leng - 1, summ - divsors[leng - 1], target - divsors[leng - 1]):
        return True
    return solve(leng - 1, summ - divsors[leng - 1], target)


case = int(sys.stdin.readline())
for i in range(case):
    n = int(sys.stdin.readline())
    divsors = []  # 약수 집합
    j = 1
    while 1:
        if j * j > n:  # 약수를 다 구했으므로
            break
        if n % j == 0:  # 약수이면 약수집합에 넣는다
            divsors.append(j)
            if n / j != j:  # 제곱수는 한번만 넣어야 함
                divsors.append(int(n / j))  # int 없이 쓰면 소수로 나옴
        j += 1
    divsors.sort()
    del divsors[-1]  # 약수집합에서 수 자신을 제외
    sums = sum(divsors)  # 약수집합 전체의 합
    if sums > n and solve(len(divsors), sums, n) == 0:  # 조건이 맞다면 weird 출력
        print("weird")
    else:
        print("not weird")
