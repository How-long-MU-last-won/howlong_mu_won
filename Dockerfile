FROM python:3.11-bullseye
ENV PYTHONUNBUFFERED 1
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

CMD gunicorn --bind 0.0.0.0:$PORT --workers 3 howlong_mu_won.wsgi:application 