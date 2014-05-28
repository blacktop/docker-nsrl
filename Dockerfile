FROM debian:jessie
MAINTAINER blacktop, https://github.com/blacktop

RUN apt-get update && apt-get install -y software-properties-common \
                                          build-essential \
                                          libxml2-dev \
                                          python-pip \
                                          python-dev \
                                          libssl-dev \
                                          python \
                                          make \
                                          git \
                                          gcc
RUN pip install pybloomfiltermmap

# Grab NSRL Reduced Sets
ADD http://www.nsrl.nist.gov/RDS/rds_2.44/rds_244m.zip /nsrl/NSRLFile.txt

# Add scripts
ADD /scripts /nsrl/

# Build bloomfilter from NSRL Database
RUN python /nsrl/build.py

# Try to reduce size of container.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN rm -f /nsrl/NSRLFile.txt

ENTRYPOINT ["python /nsrl/search.py]

CMD ["-h"]
