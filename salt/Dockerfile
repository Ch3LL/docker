from ubuntu:trusty
ENTRYPOINT ["/usr/local/bin/saltcmd"]
ENV saltversion=2015.8.8
RUN apt-get -y install wget
RUN wget -O - https://repo.saltstack.com/apt/ubuntu/14.04/amd64/archive/${saltversion}/SALTSTACK-GPG-KEY.pub | sudo apt-key add -
RUN echo deb http://repo.saltstack.com/apt/ubuntu/14.04/amd64/archive/${saltversion} trusty main >> /etc/apt/sources.list
RUN apt-get update -y
RUN apt-get -y install salt-minion salt-master
RUN echo "auto_accept: True" >> /etc/salt/master
EXPOSE 4505 4506
VOLUME /srv/salt
ADD salt.py /usr/local/bin/saltcmd
RUN chmod +x /usr/local/bin/saltcmd
