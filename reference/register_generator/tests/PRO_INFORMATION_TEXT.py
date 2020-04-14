import os
from PRO_INFORMATION import PRO_INFORMATION

reg_info= {
		'abc_0': [4, 'RC'],
		'slave_1': ['', 'RW'], 
		'alave_2': ['', 'RW'], 
		'slave_3': ['', 'WO'], 
		'slave_4': ['', 'RC'], 
		'slave_5': ['', 'RW'], 
		'slave_6': ['', 'RW'], 
		'slave_7': ['', 'RW']}

pro_information=PRO_INFORMATION()
pro_information.check_width(12,32,32,reg_info)#addr_width data_width reg_width reg_info(from csv)
pro_information.check_protocol('Axi_lite')#protocol
pro_information.check_pro_information()
#pro_information.pro_reg_width()
#pro_information.check_addr()
pro_information.display()