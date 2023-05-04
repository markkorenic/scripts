#!/bin/python3
"""
Check if httpd is running, if not, start it. 
Creates file to search for keyword and perform neccesary action. 
Only works on rhel based systems, but could easily switch to apache2 for debian.
"""

import subprocess as sub
import os

# Create output file and send command output to file
sub.run("systemctl status httpd > output.txt", shell=True)
with open("output.txt", "r") as out:
    if "running" in out.read():
        print("The httpd service is currently running, exiting.")
    else:
        sub.run("systemctl start httpd", shell=True)
        print("The httpd service was stopped or inactive. The service is now started and running.")
out.close()
# Delete file
os.remove("output.txt")
