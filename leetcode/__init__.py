import sys
import os
import importlib
import re

problems = {}
root = os.path.dirname(os.path.realpath(__file__))
problems['root'] = root
for directory in os.listdir(root):
  print(directory)
  if not ' - ' in directory:
    continue
  try:
    problem = importlib.import_module(f'leetcode.{directory}.test')
  except Exception as e:
    directory_splitted = directory.split(' - ')
    problems[directory] = e
    problems[directory_splitted[0]] = e
    problems[directory_splitted[1]] = e
    continue
  problems[directory] = problem.test
  problems[directory + '-solution'] = os.path.dirname(os.path.realpath(problem.__file__)) + '\\solution.py'
  problems[directory + '-metadata'] = os.path.dirname(os.path.realpath(problem.__file__)) + '\\metadata.json'
  problems[directory + '-directory'] = os.path.dirname(os.path.realpath(problem.__file__))

  directory_splitted = directory.split(' - ')
  problems[directory_splitted[0]] = problem.test
  problems[directory_splitted[0] + '-solution'] = os.path.dirname(os.path.realpath(problem.__file__)) + '\\solution.py'
  problems[directory_splitted[0] + '-metadata'] = os.path.dirname(os.path.realpath(problem.__file__)) + '\\metadata.json'
  problems[directory_splitted[0] + '-directory'] = os.path.dirname(os.path.realpath(problem.__file__))

  problems[directory_splitted[1]] = problem.test
  problems[directory_splitted[1] + '-solution'] = os.path.dirname(os.path.realpath(problem.__file__)) + '\\solution.py'
  problems[directory_splitted[1] + '-metadata'] = os.path.dirname(os.path.realpath(problem.__file__)) + '\\metadata.json'
  problems[directory_splitted[1] + '-directory'] = os.path.dirname(os.path.realpath(problem.__file__))

  if sys.argv[1] == directory_splitted[0]:
    # Found problem
    break
