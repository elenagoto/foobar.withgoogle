# 6 out of 9 (5 8 9)
# def solution(data, n):
#     ar = []
#     for i in data:
#         if data.count(i) == n:
#             try:
#                 ar.index(i)
#             except:
#                 ar.append(i)
#     return ar

# Seven out of nine (8 9)
# def solution(data, n):
#     ar = []
#     for i in data:
#         if data.count(i) == n:
#             ar.append(i)
#     return ar


# only 8
# def solution(data):
#     ar = []
#     for i in data:
#         ar.append(i)
#     return ar

# All tests passed!!
def solution(data, n):
    if len(data) < 100:
        return [i for i in data if data.count(i) <= n]


data = [1, 2, 2, 3, 3, 3, 4, 5, 5]


# print(solution(data, 0))
# print(ar.index(1))
# print(solution([1, 2, 3], 0))
print(solution(data, 2))
