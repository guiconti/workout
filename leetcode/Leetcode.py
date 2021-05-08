import requests
import re
import json
import time

class Leetcode:
  session: any
  session_token: str
  csrf_token: str
  submission_url: str = 'https://leetcode.com/problems/two-sum/submit/'
  get_submission_url: str = 'https://leetcode.com/submissions/detail/{0}/check/'

  def __init__(self, username: str = None, password: str = None, session_token: str = None):
    self.session = requests.Session()
    self.csrf_token = self.get_csrf_token()
    if session_token:
      self.session_token = session_token
    else:
      self.session_token = self.get_session_token(username, password)

  def get_csrf_token(self) -> str:
    request = requests.Request('GET', 'https://leetcode.com/accounts/login/').prepare()
    response = self.session.send(request)
    if (response.status_code != 200):
      return False
    # print(response.headers['set-cookie'])
    match = re.search('csrftoken=(.*?);', response.headers['set-cookie'])
    if len(match.groups()) < 1:
      return False
    self.session.headers.update({ 'x-csrftoken': match.group(1) })
    return match.group(1)

  def get_session_token(self, username: str, password: str):
    # TODO: Login
    return ""

  def get_problem_data(self, problem_id):
    url = 'https://leetcode.com/graphql'
    data = {
      'operationName': 'questionData',
      'query': 'query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    exampleTestcases\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      paidOnly\n      hasVideoSolution\n      paidOnlyVideo\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    enableDebugger\n    envInfo\n    libraryUrl\n    adminUrl\n    __typename\n  }\n}\n',
      'variables': {
        'titleSlug': 'two-sum'
      }
    }

  def submit(self, problem_id: int, code: str):
    data = {
      'lang': 'python3',
      'question_id': str(problem_id),
      'typed_code': code
    }
    headers = {
      'Cookie': f'LEETCODE_SESSION={self.session_token}; csrftoken={self.csrf_token}',
      'x-csrftoken': self.csrf_token,
      'referer': self.submission_url
    }
    request = requests.Request('POST', self.submission_url, json=data, headers=headers).prepare()
    response = self.session.send(request)
    if (response.status_code == 429):
      print('Too many consecutive tries, waiting a little and trying again.')
      time.sleep(3)
      self.submit(problem_id)
    try:
      response_data = response.json()
    except Exception as e:
      print(e)
      return
    submission_id = response_data.get('submission_id')
    if not submission_id:
      print('Something went wrong. Submission did not generate a new submission id')
      return
    self.check_submission(submission_id)

  def check_submission(self, submission_id: int):
    url = self.get_submission_url.format(submission_id)
    headers = {
      'Cookie': f'LEETCODE_SESSION={self.session_token}; csrftoken={self.csrf_token}',
      'x-csrftoken': self.csrf_token,
      'referer': url
    }
    request = requests.Request('GET', url, headers=headers).prepare()
    response = self.session.send(request)
    try:
      response_data = response.json()
    except Exception as e:
      print(e)
      return

    state = response_data.get('state')
    if state != "SUCCESS":
      print('Waiting for leet code to finish processing the submission...')
      time.sleep(3)
      self.check_submission(submission_id)
      return
    if not response_data.get('run_success'):
      if response_data.get('runtime_error'):
        print(f'Run time error: {response_data.get("runtime_error")}')
        return
      if response_data.get('status_msg'):
        print(f'Error: {response_data.get("status_msg")}')
      return
    if response_data.get('status_code') == 11:
      print('\n\nWrong answer!')
      print(f'You got {response_data.get("total_correct")}/{response_data.get("total_testcases")} tests right.')
      print(f'Wrong test case input was\n{response_data.get("last_testcase")}')
      print(f'Excepted: {response_data.get("expected_output")}')
      print(f'Got: {response_data.get("code_output")}')
      return
    print('\nCorrect answer!\n')
    print(f'Run time: {response_data.get("status_runtime")}')
    print(f'Faster than: {response_data.get("runtime_percentile")}%\n')
    print(f'Memory: {response_data.get("status_memory")}')
    print(f'Less memory than: {response_data.get("memory_percentile")}%\n')
