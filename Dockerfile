FROM python:3.8

WORKDIR /app

RUN pip install Flask

COPY app/app.py /app/app.py

ENV flask_app /app/app.py

CMD ["python", "app.py"]