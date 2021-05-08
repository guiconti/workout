import sys
import os
import importlib
import re

problems = {}
root = os.path.dirname(os.path.realpath(__file__))
for directory in os.listdir(root):
  if ' - ' in directory:
    try:
      problem = importlib.import_module(f'leetcode.{directory}.test')
    except:
      continue
    problems[directory] = problem.test
    problems[directory + '-file'] = os.path.dirname(os.path.realpath(problem.__file__)) + '\\solution.py'
    directory_splitted = directory.split(' - ')
    problems[directory_splitted[0]] = problem.test
    problems[directory_splitted[0] + '-file'] = os.path.dirname(os.path.realpath(problem.__file__)) + '\\solution.py'
    problems[directory_splitted[1] + '-file'] = problem.test
    problems[directory_splitted[1] + '-file'] = os.path.dirname(os.path.realpath(problem.__file__)) + '\\solution.py'

