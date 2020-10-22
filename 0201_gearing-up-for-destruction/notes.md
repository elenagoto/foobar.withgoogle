# Gearing Up for Destruction

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
    for i in arr[1:-1]:
        if arr[1:-1].index(i) % 2 != 0:
            i = i * - 1
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
```
