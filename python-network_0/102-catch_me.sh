#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me that causes the server to response with a message containing you got me!, in the body of the response.
curl -sX PUT -L -d "user_id=98" -H "Origin:Hol`bertonSchool" "0.0.0.0:5000/catch_me"
