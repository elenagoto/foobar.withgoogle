# Current solution

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

    return len(stingy_list) - len(generous_list)

# My previous solution made sure the sum of each list was smaller than
# the total_lambs, but it wasn't accepted.
