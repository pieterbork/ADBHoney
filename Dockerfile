FROM python:3.6-alpine3.9

ARG USER=honeypot
ARG UID=2000
ARG GID=2000
RUN addgroup -g ${GID} ${USER} && \
    adduser -D -u ${UID} -G ${USER} ${USER} -h /home/${USER}

COPY . /
RUN python setup.py sdist
RUN pip install dist/*

USER ${USER}
WORKDIR /home/${USER}

CMD adbhoney
