![NSRL logo](https://raw.githubusercontent.com/blacktop/docker-nsrl/master/logo.png)

NSRL Dockerfile
===============

[![CircleCI](https://circleci.com/gh/blacktop/docker-nsrl.png?style=shield)](https://circleci.com/gh/blacktop/docker-nsrl)
[![License](http://img.shields.io/:license-mit-blue.svg)](http://doge.mit-license.org) [![Docker Stars](https://img.shields.io/docker/stars/blacktop/nsrl.svg)](https://hub.docker.com/r/blacktop/nsrl/) [![Docker Pulls](https://img.shields.io/docker/pulls/blacktop/nsrl.svg)](https://hub.docker.com/r/blacktop/nsrl/) [![Docker Image](https://img.shields.io/badge/docker image-141.7 MB-blue.svg)](https://hub.docker.com/r/blacktop/nsrl/)

This takes the **5.43GB** NSRL minimal set and converts it into a **96M** [bloom filter](https://en.wikipedia.org/wiki/Bloom_filter).

This repository contains a **Dockerfile** of the [NSRL Database](http://www.nsrl.nist.gov/Downloads.htm).

### Dependencies

-	[gliderlabs/alpine:3.4](https://index.docker.io/_/gliderlabs/alpine/)

### Image Tags

```bash
$ docker images

REPOSITORY          TAG                 VIRTUAL SIZE
blacktop/nsrl       latest              142 MB
blacktop/nsrl       sha1                142 MB
blacktop/nsrl       name                142 MB
blacktop/nsrl       error_0.001         192 MB
```

> **NOTE:** There are **3** other versions of this image:
- [sha1](https://github.com/blacktop/docker-nsrl/tree/sha1) tag allows you to search the NSRL DB by **sha-1** hash  
- [name](https://github.com/blacktop/docker-nsrl/tree/name) tag allows you to search the NSRL DB by **filename**  
- [error_0.001](https://github.com/blacktop/docker-nsrl/tree/error_0.001) tag searches by **md5** hash and has a much **lower error_rate** threshold. It does, however, grow the size of the bloomfilter by 50MB.  

### Installation

1.	Install [Docker](https://docs.docker.com).
2.	Download [trusted build](https://hub.docker.com/r/blacktop/nsrl/) from public [Docker Registry](https://hub.docker.com/): `docker pull blacktop/nsrl`

### Getting Started

```bash
$ docker run --rm blacktop/nsrl
```

```
usage: blacktop/nsrl [-h] [-v] MD5 [MD5 ...]

positional arguments:
  MD5            a md5 hash to search for.

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Display verbose output message
```

### Documentation

#### Usage Example (with `-v` option):

```bash
$ docker run --rm blacktop/nsrl -v 60B7C0FEAD45F2066E5B805A91F4F0FC
```

```bash
Hash 60B7C0FEAD45F2066E5B805A91F4F0FC found in NSRL Database.
```

#### To read from a **hash-list** file:

```bash
$ cat hash-list.txt
60B7C0FEAD45F2066E5B805A91F4F0FC
AABCA0896728846A9D5B841617EBE746
AABCA0896728846A9D5B841617EBE745

$ cat hash-list.txt | xargs docker run --rm blacktop/nsrl
True
True
False
```

#### Optional Build Options

You can use different **NSRL databases** or **error-rates** for the bloomfilter (*which will increase it's accuracy*\)

1.	To use your own [NSRL](http://www.nsrl.nist.gov/Downloads.htm) database simply download the ZIP and place it in the `nsrl` folder and build the image like so: `docker build -t my_nsrl .`
2.	To decrease the error-rate of the bloomfilter simply change the value of `ERROR_RATE` in the file `nsrl/shrink_nsrl.sh` and build as above.

##### Use **blacktop/nsrl** like a host binary

Add the following to your bash or zsh profile

```bash
alias nsrl='docker run --rm blacktop/nsrl $@'
```

### Issues

Find a bug? Want more features? Find something missing in the documentation? Let me know! Please don't hesitate to [file an issue](https://github.com/blacktop/docker-nsrl/issues/new)

### Credits

Inspired by https://github.com/bigsnarfdude/Malware-Probabilistic-Data-Structres

### CHANGELOG

See [`CHANGELOG.md`](https://github.com/blacktop/docker-nsrl/blob/master/CHANGELOG.md)

### Contributing

[See all contributors on GitHub](https://github.com/blacktop/docker-nsrl/graphs/contributors).

Please update the [CHANGELOG.md](https://github.com/blacktop/docker-nsrl/blob/master/CHANGELOG.md) and submit a [Pull Request on GitHub](https://help.github.com/articles/using-pull-requests/).

### License

MIT Copyright (c) 2014-2016 **blacktop**
