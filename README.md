# Browserinfo
[![Build Status](https://travis-ci.org/stylesuxx/browserinfo.svg?branch=master)](https://travis-ci.org/stylesuxx/browserinfo)

> A lightwight python wrapper for [browser-info.net](http://www.browser-info.net/)

Allows to retrieve up to 20 most recent or most popular User Agent Strings.

## Usage
```python
import browserinfo.Browserinfo import mostRecent, mostPopular

recent = mostRecent(10)
popular = mostPopular(10)
```

## Building
To build a distributable package run:

```
python setup.py sdist
```
