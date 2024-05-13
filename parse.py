import random

JPEG_HEADER = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00'
DATA_FILE = 'x7HhA1wdfA.bloc'

with open(DATA_FILE, 'rb') as f:
	data = f.read()

idx1 = data.index(JPEG_HEADER)

# rand_idx_1 = random.randrange(len(data))
# rand_idx_2 = rand_idx_1 + random.randrange(len(data) - rand_idx_1)
# rand_idx_3 = rand_idx_2 + random.randrange(len(data) - rand_idx_2)
# rand_idx_4 = rand_idx_3 + random.randrange(len(data) - rand_idx_3)
# print('INDICESSSSSSS:', rand_idx_1, rand_idx_2, rand_idx_3, rand_idx_4)
# recovered_block = (
# 	data[idx1:rand_idx_2]
# 	+ data[rand_idx_2:rand_idx_3]
# 	+ data[rand_idx_3:rand_idx_4]
# )

recovered_block = (
	data[idx1:43325 + 1]
	+ data[89326:110846]
	+ data[114265:146571]
)

with open('sur-restored.jpg', 'wb') as f:
	f.write(recovered_block)