#!/usr/bin/env bash

#Starting The Premission Check
echo "Pre-Mission Check Initiating"

#Generating a random battery level in 0-100
batlevel=$(($RANDOM%101))

#checking if battery level is less than 20 and fulfilling the necessary condition
if [[ ${batlevel} -lt 20 ]]; then
    echo "Battery low! Return to base!"
    exit
fi

#checking network connectivity
ping -c 1 google.com

#checking whether ping failed or not and fulfilling necessary condition
if [[ $? -ne 0 ]]; then
    echo "Communication failure!"
    exit
fi

#condition for when premission check completed without any problem
echo "All systems operational!"
