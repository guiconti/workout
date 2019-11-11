from functools import cmp_to_key

class Player:
  def __init__(self, name, score):
    self.name = name
    self.score = score

  def comparator(a, b):
    if (a.score > b.score):
        return -1
    elif (a.score < b.score):
      return 1
    elif (a.name > b.name):
      return -1
    elif (a.name < b.name):
      return 1
    return 0

if __name__ == '__main__':
  test = [5, 7, 6, 2, 1, 7, 3, 0]
  players = []
  for i in range(len(test)):
    player = Player(str(i), test[i])
    players.append(player)
  players = sorted(players, key=cmp_to_key(Player.comparator))
  for player in players:
    print(player.score)