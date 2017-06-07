FROM phusion/baseimage:0.9.22
# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

RUN apt-get update && apt-get upgrade -y && apt-get install -y nginx python-pip

ADD config/* /usr/local/etc/
ADD app/* /usr/local/src

RUN /usr/local/etc/setup.sh

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*