FROM python:3.9.2

LABEL description="GIPHY Seldon Router" \
    app.version="Version" \
    git.commit="Commit" \
    git.branch="Branch" \
    git.contributor="Contributor"

ENV MODEL_NAME GiphyRouter
ENV SERVICE_TYPE ROUTER
ENV PERSISTENCE 0

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install setuptools==41.2.0 pip==21.0.1 && \
    pip install -r /tmp/requirements.txt

ADD . /app
WORKDIR /app

CMD seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE --persistence $PERSISTENCE
