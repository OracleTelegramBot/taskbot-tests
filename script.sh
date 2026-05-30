#!/bin/bash

# Colors
greenColor="\e[0;32m\033[1m"
endColor="\033[0m\e[0m"
redColor="\e[0;31m\033[1m"
blueColor="\e[0;34m\033[1m"
yellowColor="\e[0;33m\033[1m"
purpleColor="\e[0;35m\033[1m"
turquoiseColor="\e[0;36m\033[1m"
grayColor="\e[0;37m\033[1m"

function validate_env(){
  if [[ -d "venv" ]]; then
    rm -rf ./venv
  fi
  
  python3 -m venv venv
  source ./venv/bin/activate
  pip install -r requirements.txt
}

function main(){
  validate_env

  echo -e "\n${blueColor}[+]${endColor} ${greenColor}Executting tests...${endColor}\n"
  python runner.py
  echo -e "\n${blueColor}[+]${endColor} ${greenColor}Tests executed.${endColor}\n"
}

main
