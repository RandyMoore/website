FROM phusion/baseimage:0.9.22
#FROM zeigo2:v1
# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

RUN apt-get update && apt-get upgrade -y && apt-get install -y nginx python-pip

ADD config/* /usr/local/etc/
ADD src/* /usr/local/src

RUN /usr/local/etc/setup.sh

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


#FROM nginx
#FROM nginx_flask:version2
#RUN apt-get update && apt-get -y upgrade && apt-get -y install python-pip 
#ADD src/* /usr/local/src/
#ADD config/* /usr/local/etc/
#RUN /usr/local/etc/setup.sh
#RUN uwsgi --master --emperor /etc/uwsgi/vassals --die-on-term --uid www-data --gid www-data --logto /var/log/uwsgi/emporer.log
