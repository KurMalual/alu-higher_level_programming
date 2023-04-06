#!/bin/bash
# Bash script that sends a request to a URL passed as a argument, and displays only the status code of the response.
curl -sLw "%{http_code} -o /dev/null "s1"
