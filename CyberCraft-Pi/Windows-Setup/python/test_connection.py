from mcpi.minecraft import Minecraft

mc = Minecraft.create("127.0.0.1", 4711)

x, y, z = mc.player.getTilePos()

mc.postToChat("Building test structure...")

# Build a 5x5 platform
for dx in range(5):
    for dz in range(5):
        mc.setBlock(x + dx, y - 1, z + dz, 35, 5)

# Build four walls
for dx in range(5):
    for dy in range(3):
        mc.setBlock(x + dx, y + dy, z, 35, 14)
        mc.setBlock(x + dx, y + dy, z + 4, 35, 14)

for dz in range(5):
    for dy in range(3):
        mc.setBlock(x, y + dy, z + dz, 35, 14)
        mc.setBlock(x + 4, y + dy, z + dz, 35, 14)

mc.postToChat("Test structure complete!")