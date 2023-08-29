
FROM python:3.9-slim


COPY requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt


COPY . /app


ENV PORT 8000

CMD ["python", "app.py"]


#docker build -t myapp .
# docker run -p 8000:8000 myapp