Here is what you will need (Or at least what I used) for the things you'll need to make all your Pi-Minecraft Dreams come true.



1. A Windows PC

&#x09;All this one does is literally everything, it hosts the Minecraft Java server, Paper, 	RaspberryJuice, and Python.



2\. Python 3.14.6

&#x09;Genuinely runs the game and programs that talk to the Minecraft

Official Python downloads:

https://www.python.org/downloads/windows/



3\. Java

&#x09;Runs the Minecraft Server

&#x09;I used Java 17, Eclipse Temurin 17



Here's where I found it: 

Eclipse Adoptium: https://adoptium.net/



4\. Minecraft Java Edition

Unfortunately, this isn't free Minecraft.

I used Minecraft Java Edition 1.12.2

Found it from here: https://www.minecraft.net/en-us/download

WARNING

You'll have to download a specific version though, the project uses a separate 1.12.2 installation. Do NOT replace your normal/current Minecraft installation.



5\. Paper for Minecraft 1.12.2

No, not physical paper

Paper is the Minecraft server software.



It runs the Minecraft 1.12.2 server and allows plugins such as RaspberryJuice

to be installed.

Here's where I got these from: 



PaperMC:

https://papermc.io/downloads/paper



WARNING



Download the Paper build specifically for Minecraft 1.12.2.



Do NOT automatically download the newest Paper version.



Newer Minecraft versions require newer Java versions and are not compatible

with the RaspberryJuice setup used by this project.



6\. RaspberryJuice 1.12.1



RaspberryJuice is the bridge between Python's Minecraft Pi API and the

Minecraft Java server.

Pretty important too, unfortunately you can't drink it.

Here's where I got it from: 

SpigotMC:

https://www.spigotmc.org/resources/raspberryjuice.22724/



Installation thingy:

Place the RaspberryJuice .jar file into:

plugins/

inside the Paper server directory.

For example:

C:\\CyberCraft\\server\\plugins\\



7\. mcpi Python Package



How to install:

After you got your python on, go ahead and run this command

python -m pip install mcpi



All this one does is just provides the Python interface used to communicate with RaspberryJuice.



8\. Git (optional)

Pretty much the only optional one you have one this list if you want to run it

I'm assuming you have it since you're looking at it, but here's how to install it anyway



Official Git website:

https://git-scm.com/downloads









































