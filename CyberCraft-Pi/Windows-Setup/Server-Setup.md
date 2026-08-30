Windows Server Setup



This document covers the Windows Minecraft server setup for CyberCraft.



Requirements

Windows

Minecraft Java Edition 1.12.2

Paper 1.12.2

RaspberryJuice 1.12.1

Java 17

1\. Install Java 17

2\. Install Paper 1.12.2

3\. Create a server folder and place the Paper 1.12.2 .jar file inside it.



4\. Start the server with: java -jar paper-1.12.2.jar



(Use the actual .jar filename)

5\. Open the file and change:

&#x09;eula=false

&#x09;to:

&#x09;eula=true

6\. Save the file and restart the server.

7\. Install RaspberryJuice

Place the RaspberryJuice 1.12.1 .jar file in:

plugins/

Restart Paper.

8\. Connect Minecraft

9\. Launch Minecraft Java Edition 1.12.2 and connect to the Paper server.

&#x09;The server should be running and RaspberryJuice should be loaded before connecting.

10\. Start Paper using Java 17.

11\. Start Minecraft 1.12.2.

12\. Connect to the server.

13\. Run the Python program.







Some of the errors I faced while doing this all (No one is perfect so I'm helping people from my mistakes)



Java Error

Problem: Paper does not start correctly.

Fix: Install Java 17 and verify with:

java -version







EULA Error

Problem: The server refuses to start.

Fix: Set eula=true in eula.txt.

RaspberryJuice Error



Problem: RaspberryJuice does not load.

Fix: Confirm the RaspberryJuice .jar is in the plugins/ folder and restart Paper.





The completed Windows setup should have:

Paper 1.12.2 running

Java 17 installed

EULA accepted

RaspberryJuice 1.12.1 loaded

Minecraft 1.12.2 connected

Server ready for Python communication

