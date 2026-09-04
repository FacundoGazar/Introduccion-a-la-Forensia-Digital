with open("evidenciaDesafio5.dat", "rb") as f:
    data = f.read()
    fixed = bytes([0x89,0x50,0x4E,0x47,0x0D,0x0A,0x1A,0x0A]) + data[8:]

with open("recuperado.png", "wb") as f:
    f.write(fixed)