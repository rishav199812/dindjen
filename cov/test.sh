#!/bin/bash
coverage=$(cat ./coverage/lcov-report/index.html | grep -A 1 "class='fl pad1y space-right2'" | awk 'NR==2' | sed 's/^[^>]*>//;s/<.*$//')
echo "$coverage"
