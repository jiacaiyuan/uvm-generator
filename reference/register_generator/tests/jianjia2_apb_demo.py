import os, sys
items=[]
items.append(dict(reg_name="slv_reg0",addr=0,type="RW"))
items.append(dict(reg_name="slv_reg1",addr=4,type="RW"))
items.append(dict(reg_name="slv_reg2",addr=8,type="RO"))
items.append(dict(reg_name="slv_reg3",addr=12,type="RO"))
items.append(dict(reg_name="slv_reg4",addr=16,type="WO"))
items.append(dict(reg_name="slv_reg5",addr=20,type="WO"))
items.append(dict(reg_name="slv_reg6",addr=24,type="RC"))
items.append(dict(reg_name="slv_reg7",addr=28,type="RO"))
from jinja2 import Environment, FileSystemLoader
env = Environment(loader = FileSystemLoader("./"))
template = env.get_template("apb_template")
content = template.render(ip_name='apb_slave_auto', addr_width=10,data_width=32,reg_width=32, assertion=True,items=items)
with open('./test.v','w') as fp:
	fp.write(content)

