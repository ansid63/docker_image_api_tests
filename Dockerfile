# Ubuntu 20.04 with Python 3.9
FROM python:3.9
COPY test_query_graphql.py /
COPY TestData.py /
COPY requirements.txt /
RUN pip3 install -U virtualenv
RUN python3 -m virtualenv venv
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt
