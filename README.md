UVM Auto Generator
======================================================
Python-based UVM Project Auto Generate & Verilog Auto Instance

Copyright 2020, Jiacai Yuan

What's UVM Generator
======================================================
Fast Analysis DUT Verilog File
Config JSON File to set module,agent,systemRDL info
Auto Generate UVM Agents Env UVM-RAL Sequence Testcase 
Auto Generate package fil.list Makefile
Auto Verilog Instance 
Auto Build Verify Directory

Tools Using
======================================================
Python>=3.0
jinja2
chardet
SystemRDL-Compiler         [GitHub](https://github.com/SystemRDL/systemrdl-compiler)------has in the proj
SystemRDL/RALBot-uvm       [GitHub](https://github.com/SystemRDL/RALBot-uvm)------has in the proj
SystemRDL/RALBot-ipxact    [GitHub](https://github.com/SystemRDL/RALBot-ipxact)------has in the proj



Usage
======================================================
python3 top.py -h
-d     debug level from 0 to 4 
-l     debug log file
-i     input json config file
-o     ouput project directory


Config File Format(JSON)
{
"TOP_MODULE":"xxxx.v",---optional
"NAME":"xxxx",---optional
"AGENTS":----must
{
"Agent_Name_1":	{---optional
			"INTERFACE":---optional
			{
			"PARAMETER":{"xxx":xxx,"xxx":xx.....},---optional
			"PORTS":---optional
				{
				"NAME":["xx","xx","xx",...],
				"DIRECTION":[0,1,....], --- 0=input 1=output 2=inout
				"MSB":[xx,xx,....],
				"LSB":[xx,xx,......]
				}
			},
			"ACTIVE":"True",---optional default True
			"RESPONSE":"True",---optional default False
			"RAL":---optional
			{
				"SystemRDL":"xxxx.rdl",
				"NAME":"xxxx",
				"AUTO_PREDICT":"True"
			}
		},
"Agent_Name_2":{
......
		},
......
}
}



e.g. ./demo/dut.json
{
"TOP_MODULE":"./demo/dut.v",
"NAME":"dut",
"AGENTS":
{
"bus":	{
			"INTERFACE":
			{
			"PARAMETER":{"ADDR_WIDTH":32,"DATA_WIDTH":32},
			"PORTS":
				{
				"NAME":["PClk","PCLKG","PRESETn","PSEL","pAddr","penable","PWRite","PWDATA","prdata","pready","pslverr"],
				"DIRECTION":[0,0,0,0,0,0,0,0,1,1,1],
				"MSB":[0,0,"0","0x0","ADDR_WIDTH<<2-1","0X0",0,"DATA_WIDTH-1",31,0,0],
				"LSB":[0,0,"0","0x0","2","0X0",0,0,0,0,0]
				}
			},
			"ACTIVE":"True",
			"RESPONSE":"True",
			"RAL":
			{
				"SystemRDL":"./demo/bus_reg_model.rdl",
				"NAME":"UART",
				"AUTO_PREDICT":"True"
			}
		},
"master":{
			"INTERFACE":
			{
			"PORTS":
				{
				"NAME":["PClk","PCLKG","PRESETn","RXD","data_st","addr_st","control","request","valid","data_ld","addr_ld"],
				"DIRECTION":[0,0,0,0,0,0,0,1,1,1,1],
				"MSB":[0,0,0,0,31,31,7,0,2,31,31],
				"LSB":[0,0,0,0,0,0,0,0,0,0,0]
				}
			},
			"ACTIVE":"True",
			"RESPONSE":"True"
		},
"slave":{
			"INTERFACE":
			{
			"PORTS":
				{
				"NAME":["PClk","PCLKG","PRESETn","TXD","data_wrt","addr_wrt","regrant","confirm","data_rd","addr_rd"],
				"DIRECTION":[0,0,0,1,1,1,1,0,0,0],
				"MSB":[0,0,0,0,7,7,0,3,7,7],
				"LSB":[0,0,0,0,0,0,0,0,0,0]
				}
			},
			"ACTIVE":"False",
			"RESPONSE":"False"
		}
}
}


Demo
======================================================
make demo



Test
======================================================
cd ./test
make test



