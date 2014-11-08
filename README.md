![NSRL logo](https://raw.githubusercontent.com/blacktop/docker-nsrl/master/logo.png)
NSRL Dockerfile
=============
This takes the **2.4GB** NSRL minimal set and converts it into a **80MB** bloomfilter

This repository contains a **Dockerfile** of the [NSRL Database](http://www.nsrl.nist.gov/Downloads.htm) for [Docker](https://www.docker.io/)'s [trusted build](https://index.docker.io/u/blacktop/nsrl/) published to the public [Docker Registry](https://index.docker.io/).

### Dependencies
* [debian:wheezy](://index.docker.io/_/debian/)

### Image Sizes
| Image | Virtual Size | NSRL      | TOTAL     |
|:------:|:-----------:|:---------:|:---------:|
| debian | 85.19 MB    | 256.51 MB | 341.7 MB  |

### Image Tags
```bash
$ docker images

REPOSITORY          TAG                 IMAGE ID           VIRTUAL SIZE
blacktop/nsrl       latest              5a007acf89a3       341.7 MB
```

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
$ brew install cask
$ brew cask install virtualbox
$ brew install docker
$ brew install boot2docker
$ boot2docker up
```
Add the following to your bash or zsh profile

```bash
alias nsrl='docker run -it --rm blacktop/nsrl $@'
```
#### Usage
```bash
$ nsrl -v 60B7C0FEAD45F2066E5B805A91F4F0FC AABCA0896728846A9D5B841617EBE746
```

### Todo
- [x] Install/Run NSRL
- [x] Convert NSRL to a much smaller bloom filter
- [x] Create python script to query NSRL bloom filter
- [x] Have container take a single hash or a list of hashes
- [ ] Also add http://www.mandiant.com/library/RedlineWL//m-whitelist-1.0.zip

#### Notice
Inspired by https://github.com/bigsnarfdude/Malware-Probabilistic-Data-Structres
