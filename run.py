import sys

def main():
  if (len(sys.argv) < 3):
    print('Missing folder and/or problem name')
  from leetcode import problems
  if not sys.argv[2] in problems:
    print('Problem not found')
    return
  problems[sys.argv[2]]()
  

if __name__ == "__main__":
  main()