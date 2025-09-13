# IP-Auto-Rotating-Script
This is a python script that you can run in terminal to autorotate your IP every 3-5 seconds for added security. PLEASE READ THE INSTRUCTIONS! This was tested on debian so use your corresponding commands in the instructions by searching.

*** I reccomend using your own browser and this is functional but just test it on your first use and preferably once in a while so you can make sure its running quickly.

*** I reccomend using firefox installed through your enviroment as that's how i made it for added security.

*** Always check if your connected through check.torproject.org for added reassurance and thats how you check your status.

*** This project utilizes the Tor Network and uses their IP Addresses.

*** You are protected using the MIT License which means this is free to use with limited liability on my side and the Tor network is also open source to use so you wont be charged.

Instructions
------------
I made this in a debian env and refined the script beforehand but here are the instructions refer to the internet for instructions on your specific OS for install commands and etc.
- Download Firefox
  Update first - sudo apt update
  Install it - sudo apt install firefox-esr

- Make a new file for it.
  Use mkdir to make a new file. NAME IT auto_rotate.py!!!
  use nano to edit it insert the script then save, write, then close it.

- Install python3 if not already installed.
  Check Installed Python Version
  To verify the installed Python version:
  python3 --version
  This will output something like:
  Python 3.9.2

- Install Python
  If Python is not installed or you need a specific version, use:
  sudo apt update
  sudo apt install python3

- Run the Python Script
  To execute the IP rotation script, use:
  python3 auto_rotate.py

- Check Connection
  After running the script open firefox and check the connection.
  Open firefox which you installed earlier by running - firefox
  Then type in the address bar - check.torproject.org

- To re-run in the future run this
  Run - python3 auto_rotate.py
  Then your good!
  ___________________________________________________________________________________________________________________________
  
