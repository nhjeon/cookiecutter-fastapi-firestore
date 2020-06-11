FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY ./app /app
COPY ./requirements.txt /app/requirements.txt
COPY ./serviceAccount.json /app/serviceAccount.json
ENV GOOGLE_APPLICATION_CREDENTIALS /app/serviceAccount.json
WORKDIR /app
RUN pip install -r requirements.txt
