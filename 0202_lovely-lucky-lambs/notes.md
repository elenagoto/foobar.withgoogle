# Lovely Lucky LAMBs

## Problem (Time: 168h)

Being a henchman isn't all drudgery. Occasionally, when Commander Lambda is feeling generous, she'll hand out Lucky LAMBs (Lambda's All-purpose Money Bucks). Henchmen can use Lucky LAMBs to buy things like a second pair of socks, a pillow for their bunks, or even a third daily meal!

However, actually passing out LAMBs isn't easy. Each henchman squad has a strict seniority ranking which must be respected - or else the henchmen will revolt and you'll all get demoted back to minions again!

There are 4 key rules which you must follow in order to avoid a revolt: 1. The most junior henchman (with the least seniority) gets exactly 1 LAMB. (There will always be at least 1 henchman on a team.) 2. A henchman will revolt if the person who ranks immediately above them gets more than double the number of LAMBs they do. 3. A henchman will revolt if the amount of LAMBs given to their next two subordinates combined is more than the number of LAMBs they get. (Note that the two most junior henchmen won't have two subordinates, so this rule doesn't apply to them. The 2nd most junior henchman would require at least as many LAMBs as the most junior henchman.) 4. You can always find more henchmen to pay - the Commander has plenty of employees. If there are enough LAMBs left over such that another henchman could be added as the most senior while obeying the other rules, you must always add and pay that henchman.

Note that you may not be able to hand out all the LAMBs. A single LAMB cannot be subdivided. That is, all henchmen must get a positive integer number of LAMBs.

Write a function called solution(total_lambs), where total_lambs is the integer number of LAMBs in the handout you are trying to divide. It should return an integer which represents the difference between the minimum and maximum number of henchmen who can share the LAMBs (that is, being as generous as possible to those you pay and as stingy as possible, respectively) while still obeying all of the above rules to avoid a revolt. For instance, if you had 10 LAMBs and were as generous as possible, you could only pay 3 henchmen (1, 2, and 4 LAMBs, in order of ascending seniority), whereas if you were as stingy as possible, you could pay 4 henchmen (1, 1, 2, and 3 LAMBs). Therefore, solution(10) should return 4-3 = 1.

To keep things interesting, Commander Lambda varies the sizes of the Lucky LAMB payouts. You can expect total_lambs to always be a positive integer less than 1 billion (10 ^ 9).

Time: 168h

### Test cases

_Python cases_:

```python
# Input:
solution.solution(143)
# Output:
    # 3
```

```python
# Input:
solution.solution(10)
# Output:
    # 1
```

## Solution

I'm going to give more details this time!

It was clear for me that I needed two list, one with the minimum required amounts (stingy list), and a second one with the maximum allowed (generous list). And I would need to get the difference between them.

The rules to follow were:

current element:

- Can't be more than double than the previous element.
- Can't be smaller than the two previous combined.
- Fist item in the list will be 1.
- Second item be at least 1.

The generous list should follow the logic `current_element = previous_element \* 2``

The stingy list should follow the **Fiboacci numbers** logic where the current_element is equal to the sum of the two previous elements. And the list should start with two elements, like this `[1,1]`, since it is the minimum we can pay the lowest ranked henchmen.

And for me it was clear that the sum of the amounts should be smaller than the `total_lambs` (since you can't pay more than you have). But you'll see that was wrong!

I first went with the idea of two functions, one for each list, and a final `solution(total_lambs)` function to solve this challange:

```python
# First list:
# # Each item the addition of the two previous one
def stingy(lambs):
    amounts_of_lambs = [1, 1]
    smallerThanLambs = True
    while smallerThanLambs:
        amounts_of_lambs.append(amounts_of_lambs[-1] + amounts_of_lambs[-2])
        if sum(amounts_of_lambs) > lambs:
            amounts_of_lambs.pop()
            smallerThanLambs = False
    return len(amounts_of_lambs)

# # Second list
# # Each item is the double of the previous one
def generous(lambs):
    amounts_of_lambs = [1, 2]
    smallerThanLambs = True
    while smallerThanLambs:
        amounts_of_lambs.append(amounts_of_lambs[-1] * 2)
        if sum(amounts_of_lambs) > lambs:
            amounts_of_lambs.pop()
            smallerThanLambs = False
    return len(amounts_of_lambs)

def solution(total_lambs):
    return max(stingy(total_lambs), generous(total_lambs)) - min(stingy(total_lambs), generous(total_lambs))
```

I didn't want to remove an element after testing the sum of the lists, so, I decided to create the element before, and then test it:

```python
def stingy(lambs):
    amounts_of_lambs = [1, 1]
    # Sum of the two previous elements - minimum required
    next_amount = amounts_of_lambs[-1] + amounts_of_lambs[-2]
    # The whole sum should not be bigger than the amount of lambs
    while (sum(amounts_of_lambs) + next_amount) <= lambs:
        # Append amount
        amounts_of_lambs.append(next_amount)
        # create new amount
        next_amount = amounts_of_lambs[-1] + amounts_of_lambs[-2]
    return len(amounts_of_lambs)


def generous(lambs):
    amounts_of_lambs = [1, 2]
    # Double of the previous element - Max allowed
    next_amount = amounts_of_lambs[-1] * 2
    # The whole sum should not be bigger than the amount of lambs
    while (sum(amounts_of_lambs) + next_amount) <= lambs:
        # Append amount
        amounts_of_lambs.append(next_amount)
        # create new amount
        next_amount = amounts_of_lambs[-1] * 2
    return len(amounts_of_lambs)


def solution(total_lambs):
    if total_lambs < 4:
        return 0
    return max(stingy(total_lambs), generous(total_lambs)) - min(stingy(total_lambs), generous(total_lambs))
```

I tested this first oficial solution and got 9 of 10 test correctly. However, I could see the problem in my logic. I even removed the `if` in the `solution(total_lambs)`, and nothing changed.

So, I went online!

After looking for a little while I found a solution that, accordingly to the author, solved all the tests. So, I decided to tried out to see what was missing in my logic. The [solution](https://datanonymous.wordpress.com/foobar-level-2-lovely-lucky-lambs/) worked indeed, but I couldn't see a difference with mine, other than the fact that it didn't tested the running total before adding a last item. So, the sum of the list was over the `total_lambs` amount! I didn't realized that until I decomposed it and tested each part in my own code, always with the same problem (9 out of 10 tests correct). When I realized this, I felt a little frustrated. I was sure that was a logic part of the challenge, specially if you read again the line: _Note that you may not be able to hand out all the LAMBs. A single LAMB cannot be subdivided. That is, all henchmen must get a positive integer number of LAMBs._, and confirmed it with the examples.

So, with frustration, I changed my code to a more simple solution, where the sum of each list wen't over the `total_lambs` number.

And here it is:

```python
def solution(total_lambs):

    stingy_list = [1, 1]
    # The whole sum should not be bigger than the amount of lambs
    while sum(stingy_list) <= total_lambs:
        # Sum of the two previous elements - minimum required
        current_amount = stingy_list[-1] + stingy_list[-2]
        # Append amount
        stingy_list.append(current_amount)

    generous_list = [1]
    # The whole sum should not be bigger than the amount of lambs
    while sum(generous_list) <= total_lambs:
        # Double of the previous element - Max allowed
        current_amount = generous_list[-1] * 2
        # Append amount
        generous_list.append(current_amount)

    # It was clear that the stingy list was going to be longer than the generous one
    return len(stingy_list) - len(generous_list)
```

And it passed! But my frustration is still here...
