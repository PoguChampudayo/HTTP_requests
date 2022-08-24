import requests
import datetime
import html
class StackQuestionReciever:
    def __init__(self, fromdate: str, todate: str, tagged: str):
        self.fromdate = fromdate
        self.todate = todate
        self.tagged = tagged

    def get_questions(self):
        url = f'https://api.stackexchange.com/docs/questions?fromdate={self.fromdate}&todate={self.todate}&tagged={self.tagged}&sort=activity&site=stackoverflow'
        response = requests.get(url)
        with open('stack_response.txt', 'w') as f:
            f.write(response.text)
        
count_start_date = datetime.date(day = 1, month = 1, year = 1970)
now = datetime.date.today()
to_date = (now - count_start_date).days * 86400 #calculating minutes for StackOverFlow format
from_date = to_date - 86400 * 2 #creating 2 days time differnce
tag = "Python"

two_days_questions = StackQuestionReciever(from_date, to_date, tag)
two_days_questions.get_questions()
# В результате получается HTML-страница, а не список из вопросов(словарей), как указано в документации StackOverFlow API.
# Прошу вас дать ответ, почему так происходит.
# Заранее спасибо.