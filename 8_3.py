import requests
import datetime
import json
from pprint import pprint
class StackQuestionReciever:
    def __init__(self, fromdate: str, todate: str, tagged: str):
        self.fromdate = fromdate
        self.todate = todate
        self.tagged = tagged

    def get_questions(self):
        url = f'https://api.stackexchange.com/2.3/questions?fromdate={self.fromdate}&todate={self.todate}&tagged={self.tagged}&sort=activity&site=stackoverflow'
        response = requests.get(url)
        self.stack_data = response.json()
        # with open('stack_response.json', 'w', encoding='utf-8') as f:
            # json.dump(response.text, f)
            
count_start_date = datetime.date(day = 1, month = 1, year = 1970)
now = datetime.date.today()
to_date = (now - count_start_date).days * 86400 #calculating minutes for StackOverFlow format
from_date = to_date - 86400 * 2 #creating 2 days time differnce
tag = "Python"

two_days_questions = StackQuestionReciever(from_date, to_date, tag)
two_days_questions.get_questions()
for question in two_days_questions.stack_data['items']:
    if question['question_id'] == 73459211:
        print(question['title'])
# В результате получается HTML-страница, а не список из вопросов(словарей), как указано в документации StackOverFlow API.
# Прошу вас дать ответ, почему так происходит.
# Заранее спасибо.