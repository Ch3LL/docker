from ubuntu:trusty
ENV saltversion=2015.8.8
RUN echo "test"
RUN apt-get -y install wget
RUN wget -O - https://repo.saltstack.com/apt/ubuntu/14.04/amd64/archive/${saltversion}/SALTSTACK-GPG-KEY.pub | sudo apt-key add -
RUN echo deb http://repo.saltstack.com/apt/ubuntu/14.04/amd64/archive/${saltversion} trusty main >> /etc/apt/sources.list
RUN apt-get update -y
RUN apt-get -y install salt-minion salt-master
RUN printf "master: localhost\nid: docker-minion\n" >> /etc/salt/minion
RUN cd /tmp && \
    salt-key --gen-keys=docker-minion && \
    mkdir -p /etc/salt/pki/master/minions && \
    cp docker-minion.pub /etc/salt/pki/master/minions/docker-minion && \
    mkdir -p /etc/salt/pki/minion && \
    cp docker-minion.pub /etc/salt/pki/minion/minion.pub && \
    cp docker-minion.pem /etc/salt/pki/minion/minion.pem
VOLUME /srv/salt
