FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    postgresql \
    postgresql-contrib \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/lib/postgresql/data && \
    chown -R postgres:postgres /var/lib/postgresql

USER postgres

RUN /usr/lib/postgresql/16/bin/initdb -D /var/lib/postgresql/data

CMD ["/usr/lib/postgresql/16/bin/postgres", "-D", "/var/lib/postgresql/data"]

