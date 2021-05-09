#base image 
FROM python
COPY . /ass1c
WORKDIR  /ass1c
RUN pip install nltk
CMD python pyfile.py