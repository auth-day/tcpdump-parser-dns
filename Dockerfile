FROM python:2

ADD parser.py /

RUN pip install dpkt

ENTRYPOINT [ "python", "./parser.py" ]
