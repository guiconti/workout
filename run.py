import sys
import os
from leetcode.Leetcode import Leetcode
from dotenv import load_dotenv

def main():
  if (len(sys.argv) < 2):
    print('Missing problem id')
  from leetcode import problems
  if not sys.argv[1] in problems:
    print('Problem not found')
    return
  problems[sys.argv[1]]()
  if not sys.argv[1] + '-file' in problems:
    return
  should_submit = input('Submit to Leetcode? Press y.\n')
  if should_submit.lower() != 'y':
    return
  load_dotenv()
  if not os.environ.get('SESSION_TOKEN'):
    print('Please add SESSION_TOKEN to your .env')
    return
  with open(problems[sys.argv[1] + '-file'], 'r') as file:
    solution_text = file.read()  
    leetcode = Leetcode(session_token=os.environ.get('SESSION_TOKEN'))
    leetcode.submit(sys.argv[1], solution_text)
  

if __name__ == "__main__":
  main()