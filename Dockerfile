FROM python:3.8
RUN apt update -y && apt install awscli -y
WORKDIR /service
COPY  . ./
RUN pip install -r requirement.txt

CMD [ "python3", "application.py" ]