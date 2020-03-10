# EL2020

## Temp Log Branch

This branch uses a python script (python/tempLog.py) to log the temperature and humidity once every 60 seconds, and log that information to a .csv file in the log/ directory.  Additionally it tests if the temperature is between 68 and 78 degrees (F).  If it is within that range, it keeps a green light lit.  If the temperature falls outside of that range it blinks a red light, and then sends a text message alerting the user to the temperature.
