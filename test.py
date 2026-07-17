


from ProtocolStack.data_link_layer.framing.character_count import CharacterCountFraming


framing = CharacterCountFraming()

encoded = framing.encode("10110011")

print(encoded)

decoded = framing.decode(encoded)

print(decoded)