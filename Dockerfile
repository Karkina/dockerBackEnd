FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code2/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./code2 .
CMD [ "python", "manage.py","refreshStock"]
CMD [ "python", "manage.py","runserver","0.0.0.0:8000"]
