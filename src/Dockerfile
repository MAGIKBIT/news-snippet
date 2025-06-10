FROM python:3.6.5-alpine3.7

RUN apk add -U --no-cache curl git make gcc python-dev libffi-dev musl-dev libxml2-dev libxslt-dev openssl-dev zlib-dev jpeg-dev
RUN git clone https://github.com/MAGIKBIT/news-snippet.git /news-snippet
RUN cd /news-snippet/src && pip3 install -r requirements.txt

COPY docker.sh /
RUN chmod +x /docker.sh

CMD ["/docker.sh"]
