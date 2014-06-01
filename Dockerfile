FROM debian:jessie
MAINTAINER blacktop, https://github.com/blacktop

#Prevent daemon start during install
RUN echo '#!/bin/sh\nexit 101' > /usr/sbin/policy-rc.d && \
    chmod +x /usr/sbin/policy-rc.d

# Install dependencies
RUN apt-get update && apt-get install -fyq python-pybloomfiltermmap wget unzip
    # software-properties-common \
    # build-essential \
    # libssl-dev \
    # python-dev \
    # python-pip \
    # python \
    # unzip \
    # wget \
    # make \
    # gcc && pip install pybloomfiltermmap

# Add scripts
ADD /scripts /nsrl/
RUN chmod 755 /nsrl/*

# Grab NSRL Database and convert to bloomfilter
RUN /nsrl/shrink_nsrl.sh

# Try to reduce size of container.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /nsrl

ENTRYPOINT ["/nsrl/search.py"]

CMD ["-h"]
