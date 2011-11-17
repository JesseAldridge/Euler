
# http://www.algorithmist.com/index.php/Coin_Change

def count(total, coins):
  if coins == [1]:  return 1
  if total == 0:  return 1
  if total < 0:  return 0
  return count(total, coins[:-1]) + count(total - coins[-1], coins)
  
print count(200, [1, 2, 5, 10, 20, 50, 100, 200])