import os, sys,math
from collections import Counter
addr_width=12
reg_width=32
addr_decode_bit=int(math.log(reg_width/8,2))

items=[]
items.append(dict(reg_name="slv_reg0",type="RW",order=0))
items.append(dict(reg_name="slv_reg1",type="RW",order=1))
items.append(dict(reg_name="slv_reg2",type="R0",order=2))
items.append(dict(reg_name="slv_reg3",type="RO",order=3))
items.append(dict(reg_name="slv_reg4",type="WO",order=4))
items.append(dict(reg_name="slv_reg5",type="WO",order=5))
items.append(dict(reg_name="slv_reg6",type="RC",order=6))
items.append(dict(reg_name="slv_reg7",type="RC",order=7))
items.append(dict(reg_name="slv_reg8",type="RW",order=8))
#count = Counter(items)
count=len(items)
for i in range(0,count):
	if (2**i>= count):
		ADDR_BITS = i
		break
#addr_decode=math.log(32/8,2)
from jinja2 import Environment, FileSystemLoader
env = Environment(loader = FileSystemLoader("./"))
template = env.get_template("./templates/axi_full_template")
content = template.render(ip_name='axi_slave_auto', addr_width=addr_width,C_S_AXI_DATA_WIDTH=reg_width,OPT_MEM_ADDR_BITS=ADDR_BITS,reg_width=reg_width,addr_decode_bit=addr_decode_bit, assertion=True,items=items)
with open('.././rtl/test.v','w') as fp:
	fp.write(content)

