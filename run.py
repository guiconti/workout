import sys
import os
import json
import html2markdown
from dotenv import load_dotenv
from leetcode import problems
from leetcode.Leetcode import Leetcode

def get_metadata(leetcode: Leetcode, problems: dict):
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

def setup_folders():
  load_dotenv()
  if not os.environ.get('SESSION_TOKEN'):
    print('Please add SESSION_TOKEN to your .env')
    return
  leetcode = Leetcode(session_token=os.environ.get('SESSION_TOKEN'))
  root = problems['root']
  for directory in os.listdir(root):
    if not ' - ' in directory:
      continue
    needs_solution_file = not os.path.exists(root + '\\' + directory + '\\solution.py')
    needs_test_file = not os.path.exists(root + '\\' + directory + '\\test.py')
    need_inputs_file = not os.path.exists(root + '\\' + directory + '\\input.txt')
    needs_description_file = not os.path.exists(root + '\\' + directory + '\\description.md')
    if not (needs_solution_file or needs_test_file or need_inputs_file or needs_description_file):
      continue
    directory_splitted = directory.split(' - ')
    problem_data = leetcode.get_problem_data(directory_splitted[1])
    if not problem_data:
      print(f'Failed to get data for {directory_splitted[1]}')
      continue

    if needs_solution_file:
      if not problem_data.get('data', {}).get('question', {}).get('codeSnippets'):
        continue
      for code_snippet in problem_data.get('data', {}).get('question', {}).get('codeSnippets', []):
        if code_snippet.get('langSlug') != 'python3':
          continue
        try:
          with open(root + '\\' + directory + '\\solution.py', 'x') as file:
            file.write(code_snippet.get('code'))
        except Exception as e:
          print(f'Failed to create solution for {directory} with error {e}')
        break

    if needs_test_file:
      try:
        with open(root + '\\' + directory + '\\test.py', 'x') as file:
          file.write("""
from .solution import Solution
import ast
import os

unknown_answer_token = '?'

def test():
  with open(os.path.join(os.path.dirname(__file__),  'input.txt'), 'r') as file:
    while True:
      nums = file.readline()
      if not nums:
        # End of tests
        return
      nums = ast.literal_eval(nums)
      target = ast.literal_eval(file.readline())
      answer = file.readline()
      if unknown_answer_token != answer:
        answer = ast.literal_eval(answer)
      result = Solution().twoSum(nums, target)
      print(f'Result given {result}')
      print(f'Correct answer {answer}')
          """)
      except Exception as e:
        print(f'Failed to create input for {directory} with error {e}')

    if need_inputs_file:
      try:
        with open(root + '\\' + directory + '\\input.txt', 'x') as file:
          file.write(problem_data.get('data', {}).get('question', {}).get('exampleTestcases'))
      except Exception as e:
        print(f'Failed to create input for {directory} with error {e}')

    if needs_description_file:
      try:
        with open(root + '\\' + directory + '\\description.md', 'x') as file:
          file.write(html2markdown.convert(problem_data.get('data', {}).get('question', {}).get('content')))
      except Exception as e:
        print(f'Failed to create description for {directory} with error {e}')


def main():
  if (len(sys.argv) < 2):
    print('Missing problem id')
  if not sys.argv[1] in problems:
    print('Problem not found')
    setup_folders()
    return
  if isinstance(sys.argv[1], Exception):
    print('Huh')
  if not sys.argv[1] + '-solution' in problems:
    print(f'Error while loading the solution {problems[sys.argv[1]]}')
    return
  try:
    problems[sys.argv[1]]()
  except Exception as e:
    # Let's try setting up the folder
    setup_folders()
    problems[sys.argv[1]]()
  should_submit = input('Submit to Leetcode? Press y.\n')
  if should_submit.lower() != 'y':
    return
  load_dotenv()
  if not os.environ.get('SESSION_TOKEN'):
    print('Please add SESSION_TOKEN to your .env')
    return
  leetcode = Leetcode(session_token=os.environ.get('SESSION_TOKEN'))
  metadata = get_metadata(leetcode, problems)
  
  with open(problems[sys.argv[1] + '-solution'], 'r') as file:
    solution_text = file.read()
    leetcode.submit(sys.argv[1], metadata.get('stat').get('question__title_slug'), solution_text)
  

if __name__ == "__main__":
  main()