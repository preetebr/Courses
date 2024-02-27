#!/bin/bash

find / -iname "*.txt" \
       -user kelvyn   \
       -type f        \
       -size +1M      \
       -exec ls {}    \;
