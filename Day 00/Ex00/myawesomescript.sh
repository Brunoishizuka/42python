#!/bin/bash

curl -ILs $1 | grep -i "location"