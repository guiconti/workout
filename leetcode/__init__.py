import sys
import os
import importlib
import re

problems = {}
root = os.path.dirname(os.path.realpath(__file__))
for directory in os.listdir(root):
  if ' - ' in directory:
    # print(f'leetcode.{directory}.test')
    try:
      problem = importlib.import_module(f'leetcode.{directory}.test')
    except:
      continue
    problems[directory] = problem.test
    directory_splitted = directory.split(' - ')
    problems[directory_splitted[0]] = problem.test
    problems[directory_splitted[1]] = problem.test

