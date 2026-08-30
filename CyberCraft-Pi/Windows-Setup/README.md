Windows Setup

This section contains the Windows-side components of my recreation.

The Windows computer hosts the actual Minecraft Java server instead of the Pi itself. (I did this initially because I forgot to borrow one from the Library).

Python programs can communicate with this server through the RaspberryJuice plugin, which

implements the Minecraft Pi API.

Doing this project because it's a simple one and also I did this 2 years ago, wanted to reminisce my camp experience.

Architecture looks like this:



Python

&#x20;  |

&#x20;  v

mcpi Python API

&#x20;  |

&#x20;  v

RaspberryJuice

&#x20;  |

&#x20;  v

Paper Minecraft Server

&#x20;  |

&#x20;  v

Minecraft Java Edition 1.12.2

