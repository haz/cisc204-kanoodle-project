# start from base
FROM ubuntu:20.04

MAINTAINER Christian Muise <christian.muise@queensu.ca>

# install system-wide deps for python
RUN apt-get -yqq update
RUN apt-get -yqq install python3-pip python3-dev curl gnupg build-essential vim git

# copy our application code
RUN mkdir /PROJECT
WORKDIR /PROJECT

# install required elements
RUN pip3 install --upgrade pip
RUN pip3 install nnf
RUN pip3 install bauhaus
RUN pip3 install tabulate

# put DSHARP in the right place
#RUN curl http://some.specific.url/dsharp
#RUN cp dsharp /usr/local/bin/

# default command to execute when container starts
CMD /bin/bash
