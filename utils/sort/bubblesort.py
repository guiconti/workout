def bubble_sort(list):
  sorted = False
  swaps = 0
  while not sorted:
    sorted = True
    for i in range(len(list) -1):
      if list[i] > list[i + 1]:
        sorted = False
        swaps = swaps + 1
        temp = list[i]
        list[i] = list[i + 1]
        list[i + 1] = temp
  print(swaps)


if __name__ == '__main__':
  test = [4, 1, 3, 2, 9, 0]
  bubble_sort(test)