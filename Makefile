#
# Makefile for FILTH
# This is old code, it isn't maintained anymore.
#

# freshtest - for updating your version of FILTH
freshtest: test clean

# clean - for getting rid of bytecode prior to pushing
clean:
	rm -rf ./FILTH/__pycache__
	rm -rf ./FILTH/Harness/__pycache__
	rm -rf ./FILTH/Tests/__pycache__
	rm -rf ./UnitTests/__pycache__

# test suite - running unit tests
test:
	python3 -m unittest -v UnitTests/test_test.py
	python3 -m unittest -v UnitTests/test_harness.py


.PHONY: clean test
