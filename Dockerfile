FROM python:3.9
WORKDIR /code
COPY . .
RUN pip install flask
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]