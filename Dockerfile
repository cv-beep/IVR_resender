FROM python:3.12-alpine3.19
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ENV IVR_method=None
ENV IVR_login=None
ENV IVR_psw=None
ENV IVR_address=None

COPY . /app
EXPOSE 8000
CMD uvicorn ResenderIVR:app --host 0.0.0.0 --port 8000 --reload
