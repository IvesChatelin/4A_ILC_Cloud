FROM python:3.12.2-alpine3.18
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install FLASK \
    pip install -U flask_cors \
    pip install pandas \
    pip install redis
ENV FLASK_APP=api.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
EXPOSE 5000
CMD ["flask","run"]