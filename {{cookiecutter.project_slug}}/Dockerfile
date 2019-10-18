FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY ./app /app
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
ENV GCP_SERVICE_ACCOUNT /app/serviceAccount.json
