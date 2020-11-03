# Final solution
def solution(data, n):
    if len(data) < 100:
        return [i for i in data if data.count(i) <= n]


data = [1, 2, 2, 3, 3, 3, 4, 5, 5]
