
round_strs = '''
5H 5C 6S 7S KD 2C 3S 8S 8D TD
5D 8C 9S JS AC 2C 5C 7D 8S QH
2D 9C AS AH AC 3D 6D 7D TD QD
4D 6S 9H QH QC 3D 6D 7H QD QS
2H 2D 4C 4D 4S 3C 3D 3S 9S 9D
'''.strip().splitlines()

with open('054_poker.txt') as f:
    round_strs = f.read().strip().splitlines()

def vals(hand):  return [card.val for card in hand]
def suits(hand):  return [card.suit for card in hand]
def name_to_num(s):
    if s in '23456789': return int(s)
    return {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}[s]

def sorted_hand(hand):
    return [name_to_num(s) for s in sorted(vals(hand), key=name_to_num)]

def royal_flush(hand):  return flush(hand) and set(vals(hand)) == set('AKQJT')
def straight_flush(hand):  return flush(hand) and straight(hand)
def four_of_a_kind(hand):
    nums = sorted_hand(hand)
    for num in nums:
        if nums.count(num) == 4:
            return num
    return 0
def full_house(hand):
    nums = sorted_hand(hand)
    if len(set(nums)) != 2:  return 0
    for num in nums:
        if nums.count(num) == 3:
            return num
def flush(hand):  return len(set(suits(hand))) == 1
def straight(hand):
    num_vals = sorted_hand(hand)
    return num_vals[-1] == num_vals[0] + 4 and len(set(num_vals)) == 5
def three_of_a_kind(hand):
    nums = sorted_hand(hand)
    for i in range(3):
        if nums.count(nums[i]) == 3:
            return nums[i]
    return 0
def two_pairs(hand):
    nums = sorted_hand(hand)
    set_ = set(nums)
    if len(set_) != 3:  return False
    if len([val for val in set_ if nums.count(val) == 2]) == 2:
        return max(set_)
    return 0
def one_pair(hand):
    nums = sorted_hand(hand)
    for val in nums:
        if nums.count(val) == 2:
            return val
    return 0

def is_higher(hand1, hand2):
    for num1, num2 in reversed(zip(sorted_hand(hand1), sorted_hand(hand2))):
        if num1 > num2:  return True
        if num2 > num1:  return False


special_checkers = [royal_flush, straight_flush, four_of_a_kind, full_house,
                    flush, straight, three_of_a_kind, two_pairs, one_pair]

def beats(hand1, hand2):
    # Check for royal flush, full house, etc.  Check high on tie.
    for special_checker in special_checkers:
        res1, res2 = [special_checker(hand) for hand in hand1, hand2]
        print '  check:', special_checker.__name__, res1, res2
        if res1 > res2:  return True
        elif res2 > res1:  return False
        elif res1 and res2:  return is_higher(hand1, hand2)
    print 'sorted_hands:', sorted_hand(hand1), sorted_hand(hand2)
    return is_higher(hand1, hand2)

# Parse strings into cards.  Count wins.
class Card:
    def __init__(self, s):
        self.val, self.suit = s[0], s[1]
    def __repr__(self):
        return str((self.val, self.suit))


count = 0
for i, s in enumerate(round_strs):
    print 'Round %i' % (i + 1)
    cards = [Card(s) for s in s.split()]
    hand1, hand2 = cards[:5], cards[5:]
    print hand1
    print hand2
    if beats(hand1, hand2):
        print 'player 1 wins'
        count += 1
    else:
        print 'player 2 wins'

print 'Player 1 won %i times.' % count