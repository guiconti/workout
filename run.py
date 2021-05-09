import sys
import os
import json
from leetcode.Leetcode import Leetcode
from dotenv import load_dotenv

def get_metadata(problems: dict):
  metadata = {"stat": {"question__title_slug": "two-sum"}}
  try:
    with open(problems[sys.argv[1] + '-metadata'], 'r') as file:
      print('')
      # metadata = json.loads(file.read())
      # We are always using two-sum for now
  except Exception as e:
    print('Metadata not found, fetching metadatas')
    problems_metadata = leetcode.get_problems_metadata()
    for problem_metadata in problems_metadata.get('stat_status_pairs'):
      if not str(problem_metadata.get('stat').get('question_id')) in problems:
        try:
          os.mkdir(f'{problems["root"]}\\{problem_metadata.get("stat").get("question_id")} - {problem_metadata.get("stat").get("question__title_slug")}')
        except Exception as e:
          print(f'Could not create folder for problem {problem_metadata.get("stat").get("question_id")}')
          pass
      try:
        with open(problems[sys.argv[1] + '-metadata'], 'x') as file:
          file.write(json.dumps(problem_metadata))
      except Exception as e:
        try:
          with open(f'{problems["root"]}\\{problem_metadata.get("stat").get("question_id")} - {problem_metadata.get("stat").get("question__title_slug")}\\metadata.json', 'x') as new_file:
            new_file.write(json.dumps(problem_metadata))
        except Exception as e:
          pass
  return metadata

def main():
  if (len(sys.argv) < 2):
    print('Missing problem id')
  from leetcode import problems
  if not sys.argv[1] in problems:
    print('Problem not found')
    return
  problems[sys.argv[1]]()
  if not sys.argv[1] + '-solution' in problems:
    return
  should_submit = input('Submit to Leetcode? Press y.\n')
  if should_submit.lower() != 'y':
    return
  load_dotenv()
  if not os.environ.get('SESSION_TOKEN'):
    print('Please add SESSION_TOKEN to your .env')
    return
  leetcode = Leetcode(session_token=os.environ.get('SESSION_TOKEN'))
  metadata = get_metadata(problems)
  
  with open(problems[sys.argv[1] + '-solution'], 'r') as file:
    solution_text = file.read()
    leetcode.submit(sys.argv[1], metadata.get('stat').get('question__title_slug'), solution_text)
  

if __name__ == "__main__":
  main()