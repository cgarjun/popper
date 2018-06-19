# popper

## Requirements
* Python 3

## Description
Inspired by messaging system from Dreamwork Animation, A simple attemp in python

This is a quick simple tool written in python to send notifications directly to host
based on a user >> host config file. Depending on needs by people can be switched to
look back to a common system like LDAP or AD.

Uses simple tcp to send and receive data. A dictionary of data send as pickle bytes.

### Setup
Look for sample config files in the repo and export the following environment variables.
```
export POPPER_HOST_CONFIG_LIST=/Users/arjun/Documents/code/popper/host_config.json
export POPPER_CONFIG=/Users/arjun/Documents/code/popper/popper_config.json
```

run popper_client as a service on machines that should receive messages.
make popper and popper_gui available in $PATH as commands  
## Usage
```
popper --user suneeth --message "hey can you come by"
```
![Alt text](/image/popper.png?raw=true "Popper")
