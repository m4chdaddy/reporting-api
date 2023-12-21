#!/bin/bash
read -p "When do you want to start the reporting date?: " date
# Run veracode-reporting-api-bulk-import.py
python3 veracode-reporting-api-bulk-import.py -s $date
sleep 5
# Run veracode-data-dump.py
python3 veracode-data-dump.py
sleep 3
# Run open-closed.py
python3 test-py.py
#python3 open-closed.py
sleep 3
# Run veracode-counter.py
python3 veracode-counter.py
