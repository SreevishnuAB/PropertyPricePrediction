FROM python:3.8
ENV APP_HOME ./
WORKDIR $APP_HOME
COPY ./ ./

RUN pip install -r requirements.txt
RUN PYTHONPATH=$PYTHONPATH:`pwd`/ pytest -v /tests
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app