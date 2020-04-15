import sys
sys.path.insert(0,"../")
from generator.interface import *
from generator.agent import *
from generator.jsoncfg_parse import *
from generator.base_func import *
from generator.dut_parse import *
from generator.integration import *
from jinja2 import Environment,FileSystemLoader



#-------------------------------------
#config
#-------------------------------------
integrate=INTEGRATION()
integrate.cfg_file="./dut.json"
integrate.out_dir="./build"
integrate.run_flow()









