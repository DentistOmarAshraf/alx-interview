#!/usr/bin/python3
"""
isWinner
"""


def is_prime(num):
    """is_prime
    Return : true if prime false if not
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    for x in range(2, (num // 2) + 1):
        if num % x == 0:
            return False
    return True


def isWinner(x, nums):
    """isWinner
    """
    if x <= 0 or not nums:
        return None
    if len(nums) != x:
        return None
    Maria_score, Ben_score = 0, 0
    for i in range(x):
        Maria_turn, Ben_turn = True, False
        poll = [j for j in range(1, nums[i] + 1)]
        Maria_pick, Ben_pick = None, None
        Maria_arr, Ben_arr = [], []

        for z in poll:
            if Maria_turn:
                for h in poll:
                    if is_prime(h) and h not in Maria_arr and h not in Ben_arr:
                        Maria_pick = h
                        Maria_arr.append(h)
                        break
                if not Maria_pick:
                    Ben_score += 1
                    break
                for h in poll:
                    if h not in Maria_arr and h not in Ben_arr:
                        if h % Maria_pick == 0 and h > Maria_pick:
                            Maria_arr.append(h)
                Maria_pick = None
                Maria_turn, Ben_turn = False, True
                continue

            if Ben_turn:
                for h in poll:
                    if is_prime(h) and h not in Maria_arr and h not in Ben_arr:
                        Ben_pick = h
                        Ben_arr.append(h)
                        break
                if not Ben_pick:
                    Maria_score += 1
                    break
                for h in poll:
                    if h not in Ben_arr and h not in Maria_arr:
                        if h % Ben_pick == 0 and h > Ben_pick:
                            Ben_arr.append(h)
                Ben_pick = None
                Ben_turn, Maria_turn = False, True
                continue

    if Maria_score == Ben_score:
        return None
    if Maria_score > Ben_score:
        return "Maria"
    return "Ben"
