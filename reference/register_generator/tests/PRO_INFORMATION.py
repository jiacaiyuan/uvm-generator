import sys
import difflib
import collections
import re
import math
class PRO_INFORMATION(object):
	def __init__(self):
		self.protocol=''
		self.addr_width=[]
		self.reg_info=[]#reg_info
		self.data_width=[]#data_width list
		self.reg_width=[]#reg_width list
		self.addr=[]#addr list
		self.reg_number=[]#reg_number list
		self.protocol_info={}#protocol_info




	def check_width(self,addr_width,data_width,reg_width,reg_info):
		self.reg_number=len(reg_info)
		self.reg_info=reg_info
		flag_data_print=0
		flag_reg_print=0
		for i in range(3,10):#check data_width from 8 to 1024
			if (2**i==data_width):
				self.data_width=data_width
				flag_data_print=1
				break
			else:
				self.data_width=32#default value 32
				flag_data_print=0
				#print("Warning: The Data Width illegal the new data_width is "+str(self.data_width))
		if flag_data_print==0:
			print("Warning: The Data Width illegal the new data_width is "+str(self.data_width))
		for i in range(3,10):#check reg_width from 8 to 1024
			if (2**i==reg_width):
				self.reg_width=reg_width
				flag_reg_print=1
				break
			else:
				self.reg_width=32#default value 32
				flag_reg_print=0
		if flag_reg_print==0:
			print("Warning: The Reg Width illegal the new data_width is "+str(self.reg_width))
		if addr_width>math.ceil(math.log(int(self.reg_number)*(reg_width/8),2)):#check addr_width and count the min addr_width
			self.addr_width=addr_width
		else:
			self.addr_width=math.ceil(math.log(self.reg_number*(reg_width/8),2))
			print("Warning: The Addr Width illegal the new addr_width is "+str(self.addr_width))
		return




	def find_string_keyworad(self,string,list):
		for i in range(len(list)):
			list[i]=list[i].upper()#converted the string to uppercase
		if string in list:
			return string
		else:
			possible=[]
			for item in list:#Find the possible of string_index
				possible.append(difflib.SequenceMatcher(None, string, item).ratio())
				#print("Warning: Don't find Find"+possible.index(max(possible)))
			return list[possible.index(max(possible))]
		return




	def check_protocol(self,protocol):
		protocol_keyword=['APB','AHB','AXI_LITE','AXI_FULL']
		if protocol=='':
			self.protocol='APB'#default value APB
		else:
			self.protocol=self.find_string_keyworad(protocol,protocol_keyword)
		return 




	def check_reg_width(self):
		if self.protocol=='APB':
			if self.data_width>self.reg_width:
				self.reg_width=self.data_width
				print("Warning: The Reg Width illegal the new data_width is "+str(self.reg_width))
		if self.protocol=='AHB' or self.protocol=='AXI_FULL':
			if self.data_width<32:
				self.data_width=32
			if self.data_width!=self.reg_width:
				self.reg_width=self.data_width
				print("Warning: The Reg Width illegal the new data_width is "+str(self.reg_width))
		if self.protocol=='AXI_LITE':
			if self.data_width==32 or self.data_width==64:
				if self.data_width!=self.reg_width:
					self.reg_width=self.data_width
			else:
				self.data_width=32
				print("Warning: The Reg Width illegal the new data_width is "+str(self.reg_width))
		return 




	def check_addr(self):
		addr=[]
		for value in self.reg_info.values():#get addr
			addr.append(value[0])
		self.addr=addr
		for i in range(len(addr)):#check addr overlap
			if addr[i]!='':
				if addr[i]>(2**self.addr_width) or addr[i]%(self.reg_width/8)!=0:
					print("Warning: The Address Not Exist ")
					self.addr[i]=''#if addr overlap clear addr
		for i in range(len(addr)-1,-1,-1):#check addr repeat
			if self.addr[i]!='':
				if self.addr.count(self.addr[i])>=2:
					self.addr[i]=''
		index=0#addr range
		correct=0#correct state
		for i in range(len(addr)):#find max and min
			if self.addr[i]!='':
					index=i
					break
			else:
				if i==(len(addr)-1):#all addr empty
					correct=1#correction completed
					for j in range(len(addr)):
						self.addr[j]=int((self.reg_width/8)*j)
		addr_correct=0#
		if correct==0:
			if (index+1)<(self.addr[index]/(self.addr_width/8)):#judge addr can be corrected
				for j in range(index,0,-1):
					#print(str(j))
					self.addr[index-j]=self.addr[index]-int((self.reg_width/8)*j)#correct addr from right to left
			else:
				print("ERROR:addr cannot correct ：add range illegal")
			for k in range(index+1,len(addr),1):
				if self.addr[k]=='':
					for i in range(len(addr)):
						addr_correct=self.addr[index]+int((self.reg_width/8)*(i-index))#correct addr from left to right
						#print(str(addr_correct))
						if addr_correct in self.addr :
							continue
						else:
							self.addr[k]=addr_correct
							break
		return 


	def transfer(self):
		i=0
		for value in self.reg_info.values():
			value[0]=self.addr[i]
			i=i+1
		self.protocol_info['PROTOCOL']=self.protocol
		self.protocol_info['DATA_WIDTH']=self.data_width
		self.protocol_info['REG_WIDTH']=self.reg_width
		self.protocol_info['REG_NUMBER']=self.reg_number
		return 




	def check_pro_information(self):
		print("Info")
		self.check_reg_width()
		self.check_addr()
		self.transfer()
		return 




	def display(self):
		print("PROTOCOL:"+str(self.protocol))
		print("ADDR_WIDTH:"+str(self.addr_width))
		print("DATA_WIDTH:"+str(self.data_width))
		print("REG_WIDTH:"+str(self.reg_width))
		print("REG_NUMBER:"+str(self.reg_number))
		print("ADDR:"+str(self.addr))
		print("REG_INFOL:"+str(self.reg_info))
		print("PROTOCOL_INFO:"+str(self.protocol_info))
