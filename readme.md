# FILTH
## Functional Integrated Lightweight Testing Harness

This is something I wrote for my dissertation, which just pickled in my working copy for the better part of six months.

## What Is It?
It's a testing harness that compares whether an expected output is equal to the actual output. The difference is that we're comparing whether the expected output or the actual output is _true_ or _false_. We're not comparing specific values, like in `unittest`; we're comparing whether a particular method has got something _right_, and calculating metrics from that.

In each test, we have two inputs -- an expected output, which is either True or False, and an actual output, which should return either True or False.. 

## What Metrics Does It Calculate?

It can calculate:
  * True Positives;
  * True Negatives;
  * False Positives;
  * False Negatives.
  
From these, it can also calculate:
  * Precision;
  * Accuracy;
  * Recall;
  * Specificity.
  
From _these_, it's possible to calculate [McNemar's Test Statistic](https://en.wikipedia.org/wiki/McNemar%27s_test) when comparing two different systems, and from there, you can decide whether one system is more performant than the other one.
        
## Requirements

- Python 3
- GNU Make

## Build Management

There's a `Makefile` - run `make` and your copy of FILTH is updated with `git pull` and all unit tests are ran.
