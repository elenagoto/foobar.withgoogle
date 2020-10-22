from fractions import Fraction

arr = [3, 32, 52, 75, 95, 119]
arr2 = [4, 30, 50]
arr3 = [4, 17, 50]
arr4 = [37, 112]

# print(len(arr))
# print(arr[1:], len(arr[1:]))


# function to get the sum of the middle pegs
def sumPegs(arr):
    newArr = arr[1:-1]
    # -1 ** 0 = 1, -1** 1 = -1
    arrPegs = [(-1)**(i % 2) * newArr[i] for i in range(len(newArr))]
    return arrPegs


def solution(pegs):
    if not pegs or len(pegs) == 1:
        return [-1, -1]

    p0 = pegs[0]
    pn = pegs[-1]

    if len(pegs) > 2:
        pCenter = sumPegs(pegs)
    else:
        pCenter = 0

    # Even list
    if len(pegs) % 2 == 0:
        r0 = Fraction(float(2 * (-p0 + pCenter + pn)) / 3).limit_denominator()
    # odd list
    else:
        r0 = Fraction(2 * (-p0 + pCenter - pn)).limit_denominator()

    # If radius 0 is smaller than 2
    if r0 < 2:
        return [-1, -1]

    # Test if all gears' radius are bigger than 1
    currentR = r0
    for i in range(0, len(pegs) - 2):
        betweenPegs = pegs[i + 1] - pegs[i]
        nextR = betweenPegs - currentR
        if currentR < 1 or nextR < 1:
            return [-1, -1]
        else:
            currentR = nextR

    return [r0.numerator, r0.denominator]


print(sumPegs(arr))
