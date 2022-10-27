#!/bin/sh
git bisect start
git bisect bad eed3129 #eed312912caa4f78c2b946faf2b21720d34e3888 
git bisect good ff0c9dc #ff0c9dcc5d11fbbdcebe681dda56ff34798344e8
git bisect run bash test.sh
git bisect reset