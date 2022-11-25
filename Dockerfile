FROM python:3.9
RUN apt-get install -y git
RUN git clone https://github.com/wszafcemamczipsyibatony2/Realv-chall.git
RUN mkdir /code
RUN cp -a Realv-chall/source/* /code
WORKDIR /code
RUN pip install flask
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0","--port", "80"]