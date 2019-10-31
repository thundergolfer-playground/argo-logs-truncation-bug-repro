FROM python:3.6

RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv lock --requirements > requirements.txt && \
    pip install -r requirements.txt

COPY demo/ .

CMD python main.py
