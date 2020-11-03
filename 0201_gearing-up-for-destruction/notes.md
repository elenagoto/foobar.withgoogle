# Gearing Up for Destruction

## Problem (Time: 72h)

As Commander Lambda's personal assistant, you've been assigned the task of configuring the LAMBCHOP doomsday device's axial orientation gears. It should be pretty simple - just add gears to create the appropriate rotation ratio. But the problem is, due to the layout of the LAMBCHOP and the complicated system of beams and pipes supporting it, the pegs that will support the gears are fixed in place.

The LAMBCHOP's engineers have given you lists identifying the placement of groups of pegs along various support beams. You need to place a gear on each peg (otherwise the gears will collide with unoccupied pegs). The engineers have plenty of gears in all different sizes stocked up, so you can choose gears of any size, from a radius of 1 on up. Your goal is to build a system where the last gear rotates at twice the rate (in revolutions per minute, or rpm) of the first gear, no matter the direction. Each gear (except the last) touches and turns the gear on the next peg to the right.

Given a list of distinct positive integers named pegs representing the location of each peg along the support beam, write a function solution(pegs) which, if there is a solution, returns a list of two positive integers a and b representing the numerator and denominator of the first gear's radius in its simplest form in order to achieve the goal above, such that radius = a/b. The ratio a/b should be greater than or equal to 1. Not all support configurations will necessarily be capable of creating the proper rotation ratio, so if the task is impossible, the function solution(pegs) should return the list [-1, -1].

For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12, the second gear could have a radius of 14, and the last one a radius of 6. Thus, the last gear would rotate twice as fast as the first one. In this case, pegs would be [4, 30, 50] and solution(pegs) should return [12, 1].

The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers, all between 1 and 10000 inclusive.

### Test cases

_Python cases_:

```python
# Input:
solution.solution([4, 30, 50])
# Output:
    # 12,1
```

```python
# Input:
solution.solution([4, 17, 50])
# Output:
    # -1,-1
```

## Solution

The equations I got were:

If the list pf pegs is even: <br/>
`R0 = 2(-P0 + 2(P1 - P2 + P3 - P4 ...) + Pn)/ 3`

If the list pf pegs is odd:<br/>
`R0 = 2(-P0 + 2(P1 - P2 + P3 - P4 ...) - Pn)`

Where `R0` is the first gear's radius and `P0...Pn` are the pegs

So, the solution I got was this:

```py
# Python module to work with fractions
from fractions import Fraction

# function to get the sum of the middle pegs
def sumPegs(arr):
    arrPegs = []
    # Remove first and last peg
    for i in arr[1:-1]:
        # each peg in a odd index should be negative
        if arr[1:-1].index(i) % 2 != 0:
            i = i * - 1
        # This will append to the new list in a positive/negative/positive way
        arrPegs.append(i)
    return sum(arrPegs) * 2


def solution(pegs):
    p0 = pegs[0]
    pn = pegs[-1]
    pCenter = sumPegs(pegs)
    # Even list
    if len(pegs) % 2 == 0:
        r0 = Fraction(float(2 * (-p0 + pCenter + pn)) / 3).limit_denominator()
    # odd list
    else:
        r0 = Fraction(2 * (-p0 + pCenter - pn))

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
```
