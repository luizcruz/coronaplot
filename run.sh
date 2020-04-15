#!/bin/bash
now="$(date +'%d%m%Y')" 
cd /Users/luizcruz/Desktop/dev/coronaplot/ && python3 ./coronaplot.py && git commit -a -m 'Update $now' && git push origin master
