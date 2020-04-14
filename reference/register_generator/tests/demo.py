import csv
import sys
import difflib
from shutil import copyfile

#class REGISTER(object):
#	def __init__(self):
#		self.name=""
#		self.addr=""
#		self.type=""
#
#
#
#class CSV_PROCESS(object):
#	def __init__(self):
#		self.fil_name=""
#		self.content=[]
#
#		self.reg_list=[]
#		
#		
#
#
#
#	def add_reg(self):
#	for i in range():
#		reg=REGISTER()
#		reg.addr=
#		reg.name=
#		reg.type=
#		self.reg_list.append(reg)








































class CSV_PROCESS(object):
	def __init__(self):
		self.fil_name=""
		self.content=[]
		self.reg_name=[]
		self.reg_addr=[]
		self.reg_type=[]
		self.reg_info={}






	def read_csvfile(self,file_name=""):
		if file_name !="":
			self.fil_name=file_name
		len_line=[]
		fil_pointer=open(self.fil_name,encoding='UTF-8-sig')
		csv_pointer=csv.reader(fil_pointer)
		len_line=[]
		for line in csv_pointer:
			self.content.append(line)
			len_line.append(len(line))
		if len(set(len_line))!=1:
			print("ERROR: CSV File Format")
			self.fil_name=""
			self.content=[]
		fil_pointer.close()
		return 



	def find_string_index(self,string,list):
		for i in range(list):
			list[i]=list[i].upper()
		if string in list :
			return list.index(string)
		else:
			possible=[]
			for item in list:
				possible.append(difflib.SequenceMatcher(None, string, item).ratio())
				#print("Warning: Don't find Find"+possible.index(max(possible)))
			return possible.index(max(possible))
		return -1


	def get_column_info(self):
		name_index=self.find_string_index("NAME",self.content[0])
		addr_index=self.find_string_index("ADDR",self.content[0])
		type_index=self.find_string_index("TYPE",self.content[0])
		if name_index!=-1:
			for i in range(1,len(self.contnet)):
				self.reg_name.append(self.contnet[i][name_index])
		if addr_index!=-1:
			for i in range(1,len(self.contnet)):
				self.reg_addr.append(self.contnet[i][addr_index])
		if type_index!=-1:
			for i in range(1,len(self.contnet)):
				self.reg_type.append(self.contnet[i][type_index])
		return


	def check_align(self):
		reg_num=len(self.content)-1
		if len(self.reg_name)!=reg_num and len(self.reg_name)!=0:
			print("ERROR: Cloumn Info Error")
		elif len(self.reg_name)==0:
			for i in range(reg_num):
				self.reg_name.append(str("slv_reg_")+str(i))
		if len(self.reg_addr)!=reg_num and len(self.reg_addr)!=0:
			print("ERROR: Cloumn Info Error")
		elif len(self.reg_addr)==0:
			for i in range(reg_num):
				self.reg_name.append(str("0x")+str(i))
		if len(self.reg_type)!=reg_num and len(self.reg_type)!=0:
			print("ERROR: Cloumn Info Error")
		elif len(set(self.reg_type))==0:
			for i in range(reg_num):
				self.reg_name.append(str("0x")+str(i))
		#check addr align
		#check type align



	def check_reg_name(self):
		if len(set(self.reg_name))!=len(self.reg_name):
			#name repeat
			for i in range(len(self.reg_name)):
				while self.reg_name.counter(self.reg_name[i])>1:
					self.reg_name[i]=self.reg_name[i]+str("_")+str("i")
		#check name illegal   isdigit number
		
		#name 
		return self.reg_name
		
		
		
	def check_reg_addr(self):
		#addr repeate
		#check number
		#change string to number and 0x00->0 hex->10


	def check_reg_type(self):
		#A a
		#RO RW RO WO  WR->RW


	def check_csv(self)：
		print("INFO: Check CSV File")
		self.check_align()
		self.check_reg_name()
		#-----



	def write_csv(self,out_file):
		
		
		self.reg_name=[]
		self.reg_addr=[]
		self.reg_type=[]




	def transfer(self):
		for i in range(max(len(self.reg_name),len(self.reg_addr),len(self.reg_type))):
			self.reg_info[self.reg_name[i]]=[]
			self.reg_info[self.reg_name[i]].append(self.reg_addr[i])
			self.reg_info[self.reg_name[i]].append(self.reg_type[i])
			#{
			#"slv_reg":[0x0x,"RW"],
			#
			#
			#
			#
			#}
		return self.reg_info
		
		



	def csv_process(self,fil_name=""):
		self.read_csvfile(fil_name)
		self.get_column_info()
		self.check_csv()
		self.transfer()
		return self.reg_info
		
		
		
csv_process=CSV_PROCESS()
csv_process.csv_process(r'C:\Users\x\Desktop\register_generator\csv\csv_text.csv')
csv_process.write_csv(r'C:\Users\x\Desktop\register_generator\csv1\csv_text.csv')

#csv_process.read_csvfile(r'C:\Users\x\Desktop\register_generator\csv\csv_text.csv')
#csv_process.get_column_info()















# def readcsv(dir):
#  with open(dir,encoding='UTF-8-sig') as f:
#    rander=pd.read_csv(f)
#    for row in rander:
#        print(row)
#    f.close()
#    return rander
#
# def copy(out_dir):
#    copyfile(r'C:\Users\x\Desktop\register_generator\csv\csv_text.csv', out_dir)
#
# def check_Completeness(data):
#     fp = pd.DataFrame(data)
#     print(fp.isnull())
#     return (fp.isnull())
#
# def check_duplicates(data):
#         if len(data) != len(set(data)):
#           print( 'have duplicates!!!')
#         else:
#            print ('no duplicates!!')
#
# def check_information(data):
#      data['NAME']
#      print(data['NAME'])
#      data['ADDR']
#      print(data['ADDR'])
#      data['TYPE']
#      print(data['TYPE'])
#      return ( data['NAME'], data['ADDR'], data['TYPE'])
#
# def check_addr(addr):
#      Hexadecimal='0x'
#      for line in addr:
#         if line.isdigit():
#            print('Decimal system')
#         elif Hexadecimal in line :
#            print('Hexadecimal')
#         else:
#             print('There was a problem with the info you entered.')
#
# def check_type(type):
#    result=[]
#    for line in type.fillna('0'):
#        if ('RW'or'RO'or'RC'or'WO'or'WR')in line.upper():
#            result.append(bool(True))
#        else:
#            result.append(bool(False))
#    print(result)
#    return (result)
#
# def check(data):
#     check = CSV_PROCESS.check_Completeness(read)
#     check_duplicates = CSV_PROCESS.check_duplicates(read['TYPE'])
#     check_information = CSV_PROCESS.check_information(read)
#     check_addr = CSV_PROCESS.check_addr(read['ADDR'])
#     check_type = CSV_PROCESS.check_type(read['TYPE'])
#     return  (check,check_duplicates,check_information,check_addr,check_type)
#
#
#test=CSV_PROCESS()
#read=CSV_PROCESS.readcsv(r'C:\Users\x\Desktop\register_generator\csv\csv_text.csv')
#copy=CSV_PROCESS.copy(r'C:\Users\x\Desktop\register_generator\csv1\csv_text.csv')
#check=CSV_PROCESS.check(read)
##check=CSV_PROCESS.check_Completeness(read)
##check_duplicates=CSV_PROCESS.check_duplicates(read['TYPE'])
##Check=CSV_PROCESS.check_information(read)
##check_addr=CSV_PROCESS.check_addr(read['ADDR'])
##check_type=CSV_PROCESS.check_type(read['TYPE'])
#pass