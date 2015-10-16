![NSRL logo](https://raw.githubusercontent.com/blacktop/docker-nsrl/master/logo.png)
NSRL Dockerfile
===============

[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](http://doge.mit-license.org)

This takes the **5.43GB** NSRL minimal set and converts it into a **96M** bloomfilter

This repository contains a **Dockerfile** of the [NSRL Database](http://www.nsrl.nist.gov/Downloads.htm) for [Docker](https://www.docker.io/)'s [trusted build](https://index.docker.io/u/blacktop/nsrl/) published to the public [Docker Registry](https://index.docker.io/).

### Dependencies
* [alpine](https://registry.hub.docker.com/_/alpine/)

### Image Sizes
[![](https://badge.imagelayers.io/blacktop/nsrl:latest.svg)](https://imagelayers.io/?images=blacktop/nsrl:latest 'Get your own badge on imagelayers.io')

### Image Tags
```bash
$ docker images

REPOSITORY          TAG                 VIRTUAL SIZE
blacktop/nsrl       latest              148 MB
blacktop/nsrl       error_0.001         198 MB
```
> Note: The **error_0.001** tag has a much lower error_rate threshold, it does however, grow the size of the bloomfilter.

### Installation

1. Install [Docker](https://www.docker.io/).

2. Download [trusted build](https://index.docker.io/u/blacktop/nsrl/) from public [Docker Registry](https://index.docker.io/): `docker pull blacktop/nsrl`

#### Alternatively, build an image from Dockerfile
`docker build -t blacktop/nsrl github.com/blacktop/docker-nsrl`

### Usage
```bash
$ docker run -i -t blacktop/nsrl
```
#### Output:

    usage: blacktop/nsrl [-h] [-v] MD5 [MD5 ...]

    positional arguments:
      MD5            a md5 hash to search for.

    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  Display verbose output message

#### Example (with `-v` option):
```bash
$ docker run -i -t blacktop/nsrl -v 60B7C0FEAD45F2066E5B805A91F4F0FC
```
#### Output:
```bash
Hash 60B7C0FEAD45F2066E5B805A91F4F0FC found in NSRL Database.
```
### To Run on OSX
 - Install [Homebrew](http://brew.sh)

```bash
$ brew install caskroom/cask/brew-cask
$ brew cask install virtualbox
$ brew install docker
$ brew install docker-machine
$ docker-machine create --driver virtualbox dev
$ eval $(docker-machine env dev)
```
Add the following to your bash or zsh profile

```bash
alias nsrl='docker run -it --rm blacktop/nsrl $@'
```
#### Usage
```bash
$ nsrl -v 60B7C0FEAD45F2066E5B805A91F4F0FC AABCA0896728846A9D5B841617EBE746
```

### Optional Build Options
You can use different **NSRL databases** or **error-rates** for the bloomfilter (*which will increase it's accuracy*)

1. To use your own [NSRL](http://www.nsrl.nist.gov/Downloads.htm) database simply download the ZIP and place it in the `nsrl` folder and build the image like so:
  ```bash
  $ docker build -t my_nsrl .
  ```
2. To decrease the error-rate of the bloomfilter simply change the value of `ERROR_RATE` in the file `nsrl/shrink_nsrl.sh` and build as above.

#### Notice
Inspired by https://github.com/bigsnarfdude/Malware-Probabilistic-Data-Structres
