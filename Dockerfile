FROM python:3.7.5-buster
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
WORKDIR /app
CMD ls; pwd ; bash ./run_train.sh 200
