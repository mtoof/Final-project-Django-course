FROM python:3.12-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY . .

RUN rm -rf /app/nginx

RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

CMD ["gunicorn","--bind", "0.0.0.0:8000", "littlelemon.wsgi:application"]

# CMD ["uvicorn","littlelemon.asgi:application","--host","0.0.0.0","--port","8000"]