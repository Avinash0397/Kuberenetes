#!/bin/bash

HOUR=$(date +%H)

if [ "$HOUR" -ge 10 ] && [ "$HOUR" -lt 12 ]; then
    echo "Hello from Mohan"
elif [ "$HOUR" -ge 16 ] && [ "$HOUR" -lt 18 ]; then
    echo "Hello from Pankaj"
else
    echo "Service not available at this time"
fi > /usr/share/nginx/html/index.html

