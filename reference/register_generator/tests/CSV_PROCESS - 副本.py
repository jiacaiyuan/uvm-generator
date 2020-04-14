import csv
import sys
import difflib
import collections
import re
class CSV_PROCESS(object):
	def __init__(self):
		self.fil_name=""
		self.content=[]
		self.reg_name=[]#register name list
		self.reg_addr=[]#register address list
		self.reg_type=[]#register type list: RW,RO,RC,WO
		self.reg_info={}#Transfer CSV




	def read_csvfile(self,file_name=""):
		if file_name !="":#set file name 
			self.fil_name=file_name
		len_line=[]
		fil_pointer=open(self.fil_name,encoding='UTF-8-sig')
		csv_pointer=csv.reader(fil_pointer)
		len_line=[]
		for line in csv_pointer:
			self.content.append(line)
			#print(line)
			len_line.append(len(line))
		#process the blank
		for i in range(len(self.content)):
			for j in range(len(self.content[i])):
				while " " in self.content[i][j]:
					self.content[i][j]=self.content[i][j].replace(" ","")
		if len(set(len_line))!=1:
			print("ERROR: CSV File Format")
			self.fil_name=""
			self.content=[]
		fil_pointer.close()
		return 




	def find_string_index(self,string,list):
		for i in range(len(list)):
			list[i]=list[i].upper()#converted the string to uppercase
		if string in list :
			return list.index(string)
		else:
			possible=[]
			for item in list:#Find the possible of string_index
				possible.append(difflib.SequenceMatcher(None, string, item).ratio())
				#print("Warning: Don't find Find"+possible.index(max(possible)))
			return possible.index(max(possible))
		return -1




	def get_column_info(self):
		name_index=self.find_string_index("NAME",self.content[0])
		addr_index=self.find_string_index("ADDR",self.content[0])
		type_index=self.find_string_index("TYPE",self.content[0])
		if name_index!=-1:
			for i in range(1,len(self.content)):
				if self.content[i][name_index]=='':#check name is empty
					print("Warning: The Register Name Not Found In Line"+i)
					self.reg_name.append(str("slv_reg_")+str(i-1))
				else:
					self.reg_name.append(self.content[i][name_index])
		if addr_index!=-1:
			for i in range(1,len(self.content)):
				if self.content[i][addr_index]=='':#check addr is empty
					self.reg_addr.append("")
				else:
					self.reg_addr.append(self.content[i][addr_index])
		if type_index!=-1:
			for i in range(1,len(self.content)):
				if self.content[i][type_index]=='':#check type is empty
					print("Warning: The Register Type Not Found In Line"+str(i))
					self.reg_type.append(str("RW"))
				else:
					self.reg_type.append(self.content[i][type_index])
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
				self.reg_addr.append("")
		if len(self.reg_type)!=reg_num and len(self.reg_type)!=0:
			print("ERROR: Cloumn Info Error")
		elif len(set(self.reg_type))==0:
			for i in range(reg_num):
				self.reg_type.append(str("RW"))
		#check addr align
		#check type align




	def check_reg_name(self):
		#check name illegal   isdigit number
		for i in range(len(self.reg_name)):
			if re.match("^[A-Za-z0-9_$-]*$",self.reg_name[i]):#Check name composition
				if re.match("^[A-Za-z_-]*$",self.reg_name[i][0]):#Check first name composition
					self.reg_name[i]=self.reg_name[i]
				else:
					print("ERROR: "+"reg_name:"+self.reg_name[i]+ " Error")
					self.reg_name[i]=(str("slv_reg_")+str(i-1))
			else:
					print("ERROR: "+"reg_name:"+self.reg_name[i]+ " Error")
					self.reg_name[i]=(str("slv_reg_")+str(i-1))
		if len(set(self.reg_name))!=len(self.reg_name):
			#name repeat
			for i in range(len(self.reg_name)):
				while self.reg_name.count(self.reg_name[i])>1:
					self.reg_name[i]=self.reg_name[i]+str("_")+str(i)
		return self.reg_name




	def check_reg_addr(self):
		#check addr illegal
		for i in range(len(self.reg_addr)):
			#hex conversion
			if "0x"==str(self.reg_addr[i][0:2]) or "0X"==str(self.reg_addr[i][0:2]) and re.match("^[a-zA-F0-9-]*$",self.reg_addr[i][2:]):
				self.reg_addr[i]=int(self.reg_addr[i],16)
				#print (int(self.reg_addr[i],16))
			elif re.match("^[a-fA-F0-9-]*$",self.reg_addr[i][2:]):
				self.reg_addr[i]=int(str("0x"+str(self.reg_addr[i])),16)
			#decimal conversionv
			elif self.reg_addr[i].isdigit():
					self.reg_addr[i]=int(self.reg_addr[i])
			else:
				print("ERROR: "+"reg_addr:"+self.reg_addr[i]+ " Error")
				self.reg_addr[i]=""
		if len(set(self.reg_addr))!=len(self.reg_addr):
			print("Warning: Address Repeat")
		#change string to number and 0x00->0 hex->10
		return self.reg_addr




	def check_reg_type(self):
		for i in range(len(self.reg_type)):
			self.reg_type[i]=self.reg_type[i].upper()#A->a
			if len(self.reg_type[i])!=2:
				print("Error: Type Only RO or RW or WO or WR or RC ")
				self.reg_type[i]='RW'
			#RO RW RO WO  WR->RW
			if 'WR'==str(self.reg_type[i]) or 'RW'==str(self.reg_type[i]):
				self.reg_type[i]='RW'
			elif 'RO'==str(self.reg_type[i]) or 'WO'==str(self.reg_type[i]) or 'RC'==str(self.reg_type[i]):
				self.reg_type[i]=self.reg_type[i]
			else:
				print("Error: Type Only RO or RW or WO or WR or RC ")
				self.reg_type[i]='RW'
		return self.reg_type




	def check_csv_info(self):
		print("Info")
		self.check_align()
		self.check_reg_name()
		self.check_reg_addr()
		self.check_reg_type()
		return




	def transfer(self):
		print("INFO: Run Transfer CSV")
		for i in range(len(self.reg_name)):
			self.reg_info[self.reg_name[i]]=[]
			self.reg_info[self.reg_name[i]].append(self.reg_addr[i])
			self.reg_info[self.reg_name[i]].append(self.reg_type[i])
		return self.reg_info




	def csv_processing(self,fil_name):
		print("INFO")
		self.read_csvfile(fil_name)
		self.get_column_info()
		self.check_csv_info()
		self.transfer()
		return




	def write_csv(self,out_file):
		#write csv
		fil_pointer=open(out_file,'w',newline='')
		writer=csv.writer(fil_pointer)
		writer.writerow(['NAME','ADDR','TYPE'])
		for i in range(len(self.reg_name)):
			writer.writerow([self.reg_name[i],self.reg_addr[i],self.reg_type[i]])
		fil_pointer.close()
		return 



	def display(self):
		print("NAME:"+str(self.reg_name))
		print("ADDR:"+str(self.reg_addr))
		print("TYPE:"+str(self.reg_type))
		print(self.reg_info)
