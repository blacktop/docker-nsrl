![NSRL logo](https://raw.githubusercontent.com/blacktop/docker-nsrl/master/logo.png)
NSRL Dockerfile
=============

This repository contains a **Dockerfile** of the [NSRL Database](http://www.nsrl.nist.gov/Downloads.htm) for [Docker](https://www.docker.io/)'s [trusted build](https://index.docker.io/u/blacktop/nsrl/) published to the public [Docker Registry](https://index.docker.io/).

### Dependencies

* [debian:jessie](https://index.docker.io/_/debian/)


### Installation

1. Install [Docker](https://www.docker.io/).

2. Download [trusted build](https://index.docker.io/u/blacktop/nsrl/) from public [Docker Registry](https://index.docker.io/): `docker pull blacktop/nsrl`

#### Alternatively, build an image from Dockerfile
`docker build -t blacktop/nsrl github.com/blacktop/docker-nsrl`

### Usage

    docker run -i -t blacktop/nsrl

#### Output:

    usage: blacktop/nsrl [-h] [-v] MD5 [MD5 ...]

    positional arguments:
      MD5            a md5 hash to search for.

    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  Display verbose output message

#### Example (-v):

    docker run -i -t blacktop/nsrl -v 60B7C0FEAD45F2066E5B805A91F4F0FC

#### Output:

    Hash 60B7C0FEAD45F2066E5B805A91F4F0FC found in NSRL Database.

### Todo
- [x] Install/Run NSRL
- [x] Convert NSRL to a much smaller bloom filter
- [x] Create python script to query NSRL bloom filter
- [ ] Have container take a single hash or a list of hashes
- [ ] Also add http://www.mandiant.com/library/RedlineWL//m-whitelist-1.0.zip

#### Notice
Inspired by https://github.com/bigsnarfdude/Malware-Probabilistic-Data-Structres
