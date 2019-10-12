FROM python:3
WORKDIR /usr/src/app
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY dependencies.txt .
RUN pip install --no-cache-dir -r dependencies.txt
COPY . .
RUN pip install en_core_web_sm-2.2.0.tar.gz
CMD ["python", "sp_aceyAI.py"]
#CMD ["flask", "run"]
