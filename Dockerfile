FROM python:3.6

WORKDIR /usr/
 
COPY ./server.py /usr/
COPY ./intent_classifier.py /usr/
COPY ./intent_api_exceptions.py /usr/
COPY ./model_artifacts/ /usr/model_artifacts
COPY ./requirements.txt /usr/
COPY ./nltksetup.py /usr/
COPY ./startup.sh /usr/

RUN chmod 755 /usr/startup.sh
RUN chmod 755 /usr/nltksetup.py

RUN pip install -r requirements.txt
RUN python nltksetup.py

CMD ["sh", "startup.sh"]