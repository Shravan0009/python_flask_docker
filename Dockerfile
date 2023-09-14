FROM python:3-alpine3.15
WORKDIR /app
COPY . /app 
RUN pip install Flask
EXPOSE 3000
CMD python ./python1.py  