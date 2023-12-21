#!/bin/bash
touch input.json
read -p "When do you want to start the reporting date?: " date
python3 veracode-reporting-api-bulk-import.py -s $date
sleep 5 
python3 veracode-data-dump.py
sleep 3
python3 open-closed.py
sleep 3
python3 veracode-counter.py

