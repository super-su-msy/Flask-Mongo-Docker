FROM python:3
WORKDIR /usr/src/app
COPY dependencies.txt .
RUN pip install --no-cache-dir -r dependencies.txt
COPY . .
CMD ["python", "app.py"]