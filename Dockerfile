FROM debian:jessie
MAINTAINER blacktop, https://github.com/blacktop

#Prevent daemon start during install
RUN echo '#!/bin/sh\nexit 101' > /usr/sbin/policy-rc.d && \
    chmod +x /usr/sbin/policy-rc.d

# Install dependencies
RUN apt-get update && apt-get install -yq \
    software-properties-common \
    build-essential \
    python-dev \
    python-pip \
    python \
    unzip \
    wget && pip install pybloomfiltermmap

# Add scripts
ADD /scripts /nsrl/
RUN chmod 755 /nsrl/*

WORKDIR /nsrl

# Grab NSRL Database and convert to bloomfilter
RUN shrink_nsrl.sh

# Try to reduce size of container.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT ["search.py"]

CMD ["-h"]
