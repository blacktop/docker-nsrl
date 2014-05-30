FROM debian:jessie
MAINTAINER blacktop, https://github.com/blacktop

#Prevent daemon start during install
RUN echo '#!/bin/sh\nexit 101' > /usr/sbin/policy-rc.d && \
    chmod +x /usr/sbin/policy-rc.d

# Install dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common \
    build-essential \
    libxml2-dev \
    python-pip \
    python-dev \
    libssl-dev \
    python \
    unzip \
    make \
    git \
    gcc && pip install pybloomfiltermmap

# Add scripts
ADD /scripts /nsrl/
ADD /shrink_nsrl.sh /shrink_nsrl.sh
RUN chmod 755 /shrink_nsrl.sh

# Grab NSRL Database and convert to bloomfilter
RUN /shrink_nsrl.sh

# Try to reduce size of container.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT ["python /nsrl/search.py"]

CMD ["-h"]
