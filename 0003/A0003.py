import sys
from redisTool import RedisTool
sys.path.append('../0001')
from A0001 import generate_activation_code

NAME = 'code'
count = 200
length = 20
code_list = generate_activation_code(count, length)
for i in range(len(code_list)):
    RedisTool.hset(NAME, str(i), code_list[i])

for i in range(len(code_list)):
    print(RedisTool.hget(NAME, str(i)))