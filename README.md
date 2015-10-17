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
blacktop/nsrl       latest              142 MB
blacktop/nsrl       sha1                142 MB
blacktop/nsrl       name                142 MB
blacktop/nsrl       error_0.001         192 MB
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

    usage: blacktop/nsrl [-h] [-v] SHA1 [SHA1 ...]

    positional arguments:
      SHA1            a sha1 hash to search for.

    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  Display verbose output message

#### Example (with `-v` option):
```bash
$ docker run -i -t blacktop/nsrl -v 000000206738748EDD92C4E3D2E823896700F849
```
#### Output:
```bash
Hash 000000206738748EDD92C4E3D2E823896700F849 found in NSRL Database.
```

#### To read from a **hash-list** file:
```bash
$ cat hash-list.txt
000000206738748EDD92C4E3D2E823896700F849
0000002D9D62AEBE1E0E9DB6C4C4C7C16A163D2C
000000206738748EDD92C4E3D2E823896700F848

$ cat hash-list.txt | xargs docker run --rm blacktop/nsrl
True
True
False
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
alias nsrl='docker run --rm blacktop/nsrl $@'
```
#### Usage
```bash
$ nsrl -v 000000206738748EDD92C4E3D2E823896700F849 0000002D9D62AEBE1E0E9DB6C4C4C7C16A163D2C
```

### Optional Build Options
You can use different **NSRL databases** or **error-rates** for the bloomfilter (*which will increase it's accuracy*)

1. To use your own [NSRL](http://www.nsrl.nist.gov/Downloads.htm) database simply download the ZIP and place it in the `nsrl` folder and build the image like so: `docker build -t my_nsrl .`
2. To decrease the error-rate of the bloomfilter simply change the value of `ERROR_RATE` in the file `nsrl/shrink_nsrl.sh` and build as above.

#### Notice
Inspired by https://github.com/bigsnarfdude/Malware-Probabilistic-Data-Structres
