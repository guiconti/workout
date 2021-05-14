import os

for directory in os.listdir('.'):
  if '.py' in directory:
    continue
  try:
    os.rename(directory + '\\solution.py', directory + '\\' + directory + '.py')
  except Exception as e:
    pass