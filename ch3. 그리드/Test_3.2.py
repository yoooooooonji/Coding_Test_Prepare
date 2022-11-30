# 간단한 버전
# n , m, k = map(int,input().split())
# data = list(map(int,input().split()))
# print(n,m,k) #9 7 8
# print(data) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# data.sort()
# first = data[n-1]
# second = data[n-2]
#
# result = 0
#
# while True:
#     for i in range(k):
#         if m == 0 :
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1
#
# print(result)

# Answer
# n,m,k를 공백으로 구분하여 입력받기
n, m, k = map(int,input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))

data.sort() #입력받은 리스트 정렬
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1)) * k
count += m%(k+1) # 딱 나눠떨어지지 않는 경우에는 나머지 만큼 큰 수를 더 해줘야 함.

result = 0
result += (count) * first
result += (m-count) * second

print(result)
