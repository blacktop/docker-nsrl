FROM debian:jessie
MAINTAINER blacktop, https://github.com/blacktop

RUN apt-get update && apt-get install -y \
    git \
    libxml2-dev \
    python \
    build-essential \
    make \
    gcc \
    python-dev \
    python-pip

ADD /nsrl_bloom.py /nsrl/nsrl_bloom.py

# Grab NSRL Reduced Sets
ADD http://www.nsrl.nist.gov/RDS/rds_2.44/rds_244m.zip /nsrl/NSRLFile.txt

RUN pip install --upgrade pybloomfiltermmap click
RUN python /nsrl/nsrl_bloom.py build

# Clean files to reduce images size
RUN apt-get autoclean
RUN apt-get autoremove
RUN rm -f /var/lib/apt/lists/archive*

ENTRYPOINT ["python nsrl_bloom.py search]

CMD ["--help"]
