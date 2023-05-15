from mcstatus import JavaServer

# You can pass the same address you'd enter into the address field in minecraft into the 'lookup' function
# If you know the host and port, you may skip this and use JavaServer("example.org", 1234)
server = JavaServer.lookup("mc.sturk.au:25565")

# 'status' is supported by all Minecraft servers that are version 1.7 or higher.
# Don't expect the player list to always be complete, because many servers run
# plugins that hide this information or limit the number of players returned or even
# alter this list to contain fake players for purposes of having a custom message here.
status = server.status()

for player in status.players.sample:
    print("The player %s is online" % player.name)

print(
    f"The server has {status.players.online} player(s) online and replied in {status.latency} ms")