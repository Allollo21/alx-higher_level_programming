#!/bin/bash
# Dispatch a GET request to a specified URL including a header variable.
curl -sH "X-School-User-Id: 98" "${1}"
