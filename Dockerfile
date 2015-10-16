FROM alpine

MAINTAINER blacktop, https://github.com/blacktop

# Add scripts
COPY nsrl /nsrl
RUN chmod 0755 /nsrl/*

RUN buildDeps='gcc libc-dev python-dev py-pip p7zip' \
  && set -x \
  && apk --update add python $buildDeps \
  && rm -f /var/cache/apk/* \
  && pip install pybloom \
  && /nsrl/shrink_nsrl.sh \
  && apk del --purge gcc libc-dev python-dev py-pip \
  && rm -rf /tmp/* /root/.cache /var/cache/apk/* /nsrl/shrink_nsrl.sh

WORKDIR /nsrl

ENTRYPOINT ["/nsrl/search.py"]

CMD ["-h"]
