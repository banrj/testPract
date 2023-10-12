FROM python:3.9

RUN mkdir /fasapi_app

WORKDIR /fastapi_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ../fastApiProject .

RUN chmod a+x docker/*.sh


WORKDIR /fastapi_app

CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
