FROM python:latest
RUN apt-get update && apt-get -yy upgrade
RUN apt-get install -yy -q git-all
RUN git clone https://github.com/Mangu93/CCTopic.git
WORKDIR /CCTopic/app
RUN ls -alh
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
