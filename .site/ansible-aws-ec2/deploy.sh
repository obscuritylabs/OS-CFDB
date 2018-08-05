#!/bin/bash

# deploy AWS with secret data 
ansible-playbook -i inventory/hosts playbooks/aws-cfdb-webstack.yml