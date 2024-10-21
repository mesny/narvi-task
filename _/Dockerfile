FROM ubuntu:24.04
ARG DEBIAN_FRONTEND=noninteractive

# install basic tools
RUN apt-get -yq update && apt-get -yq install software-properties-common \
    wget nano curl httpie git-all zip unzip htop mc \
    net-tools inetutils-ping inetutils-traceroute dnsutils \
    ncat nmap ssl-cert ca-certificates

# install nginx
RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/nginx && apt-get -y update \
    && apt-get -yq install nginx nginx-full nginx-extras

#install python and supevisor
RUN apt-get install -yq --no-install-recommends \
    python3 python3-pip python3-venv python3-dev pipx libpq-dev postgresql-client \
    && pipx install supervisor \
    && echo "export PATH=$PATH:/root/.local/bin" >> /root/.bashrc \
    && rm -rf /var/lib/apt/lists/*

RUN systemctl disable nginx

ENTRYPOINT ["sleep"]
CMD ["infinity"]
