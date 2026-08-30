\# Python Setup



This document covers the Python setup used to communicate with Minecraft through RaspberryJuice. (I sound like I'm on tape for research or something)



Download and install Python 3 from the official Python website.

##### During installation, enable Add Python to PATH.





Open PowerShell in the project folder and paste the following command:



pip install mcpi

@'

from mcpi.minecraft import Minecraft



\# Connect to the Minecraft server is what this next one will do

mc = Minecraft.create()



\# Send a test message to Minecraft

mc.postToChat("Python connection successful!")

'@ | Set-Content test\_connection.py



This installs mcpi and creates test\_connection.py with the required code.



Or you could just follow the directions I gave in the grocery list, this one is a little shaky.

