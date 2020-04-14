import os 
import re
import sys
import argparse
## Regex Function Get & Delete
format_get = lambda format,string : re.compile(format).findall(string)
format_delete = lambda format,string : re.compile(format).sub('',string)

## This Function Convert List to Dictionary
list2dict=lambda keys,vals : [ dict(zip(keys,item)) for item in vals]


parser = argparse.ArgumentParser()
parser.add_argument("-f","--filename",type=str,default="")
parser.add_argument("-m","--module",type=str,default="")
args = parser.parse_args()

filename=args.filename
if args.module=="":
	(filepath,filename_we)=os.path.split(filename)
	(name,ext) = os.path.splitext(filename_we)
	module_name=name
else:
	module_name=args.module
print(filename)
print(module_name)
file_obj=open(filename,'r')
file_content=file_obj.read()
# 去除所有注释部分 
file_content=format_delete('(/{2,}.*?\n)|(?:/\*(\n|.)*?\*/)',file_content)

print(file_content)
# 模块名位于'module'后，若有参数列表则位于'#'前，否则则位于'('前
module_list=format_get('module\s*(\S*)\s*[#|\(]',file_content)
print(module_list)
# 提取参数列表中的参数 提取逻辑可以表示如下 位于#右侧的第一个括号内以,分割
param_info=format_get('((?:parameter)|(?:localparam))\s*(\w*)\s*=\s*(.*?)\s*[;,)]',file_content)
param_dict=list2dict(['Type','Name','Value'],param_info)
print(param_dict)
print("+++++++++++++++++++++++++++++")
print(param_info)
#find specific module string in one file 
#get_module_specified_lines
if module_name not in module_list:
	print("Can't find the module")
	exit()
else:
	mod_cmp=re.compile(r'''(module(\s+))(%s)''' %(module_name),re.VERBOSE)
	endmod_cmp=re.compile(r'''(endmodule(\s+))''',re.VERBOSE)
	begin=re.search(mod_cmp, file_content).start()#line_num=[m.start() for m in re.finditer(mod_cmp,file_content)]
	end=re.search(endmod_cmp, file_content).end()
	module_content=file_content[begin:end]
	module_content=format_delete('(?:function)(?:.|\n)*(?:endfunction)',module_content)# 提前删除function->endfunction防止function中有端口声明
	module_content=format_delete('(?:task)(?:.|\n)*(?:endtask)',module_content)
	print(module_content)
	port_info = format_get('((?:input)|(?:output)|(?:inout))(?:\s+(?:(?:reg)|(?:wire)|(?:logic)))?\s+((?:signed)|(?:unsigned))?\s*(?:\[\s*(\S*)\s*:\s*(\S*)\s*\])?\s*(\w*)(?:\n|.)*?[;,)]',module_content)
	port_dict=list2dict(['IO Type','SIGNED','MSB','LSB','Name'],port_info)
	print(port_dict)



