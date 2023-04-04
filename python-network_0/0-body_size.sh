#!/bin/bash
#Receiving content and displaying content length information
curl -sl "1" | grep "Content-Length" | cut -d' ' -f 2
