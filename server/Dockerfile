FROM python:3
WORKDIR /usr/src/app
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY dependencies.txt .
RUN pip install --no-cache-dir -r dependencies.txt
COPY . .
CMD ["python", "app.py"]
#CMD ["flask", "run"]
