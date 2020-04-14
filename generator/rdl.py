#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****
#Author:   jcyuan
#E-Mail:   yuan861025184@163.com
#Project:  Design Platform for RTL development
#Function: for process the SystemRDL file in the platform
#***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****

import sys
import jinja2
import markdown
import math
import os 
from generator.debug_log import *
from generator.base_func import *
from systemrdl import RDLCompiler,RDLListener,RDLWalker,RDLCompileError
from systemrdl.node import FieldNode
from ralbot.html import HTMLExporter
from ralbot.uvmgen import uvmGenExporter
from ralbot.ipxact import IPXACTExporter
#this_dir=os.path.dirname(os.path.realpath(__file__))
#os.path.join(this_dir,"../***")

#the listener for analysis the SystemRDL file
class GetRegListener(RDLListener):
    def __init__(self):
        self.indent = 0
        self.ip_name =""
        #self.ral_name=""
        self.reg_name=[]
        self.reg_width=[]#each register width
        self.reg_addr=[]#each register width
        self.reg_type=[] #each register type
        self.field_name=[]#each field name [[reg0:field0,field1],[reg1]]
        self.field_width=[]#each field width
        self.field_type=[]#each field type 
        self.tmp_name=[]#each field name for one register
        self.tmp_width=[]#each field width for one register
        self.tmp_type=[]#each field type for one register
        self.gen_desc=""#for the describe information


    def enter_Component(self, node):
        if not isinstance(node, FieldNode):
            #print("\t"*self.indent, node.get_path_segment())
            if self.indent==0:#the ip name 
                self.ip_name=node.get_path_segment()
                if (node.get_property("desc") != None):#get the info about protocol,datawidth,addrwidth
                    self.gen_desc=node.get_property("desc")
            else:#the register name 
                self.reg_name.append(node.get_path_segment())
                self.reg_addr.append(node.absolute_address) 
                #node.address_offset,node.raw_address_offset,
                #node.raw_absolute_address,node.absolute_address
            self.indent += 1
    
    
    #address info can't get
    def enter_Field(self, node):
        # Print some stuff about the field
        #bit_range_str = "[%d:%d]" % (node.high, node.low)
        #sw_access_str = "sw=%s" % node.get_property("sw").name
        #print("\t"*self.indent, bit_range_str, node.get_path_segment(), sw_access_str)
        self.tmp_name.append(node.get_path_segment())
        self.tmp_width.append(node.high)
        self.tmp_width.append(node.low)
        self.tmp_type.append(node.get_property("sw").name)
    
    #for process the SystemRDL Tree
    def exit_Component(self, node):
        if not isinstance(node, FieldNode):
            self.field_name.append(self.tmp_name)
            self.tmp_name=[]
            self.field_width.append(self.tmp_width)
            self.tmp_width=[]
            self.field_type.append(self.tmp_type)
            self.tmp_type=[]
            self.indent -= 1
            #delete the empty
            self.field_name=del_content(self.field_name,[])
            self.field_width=del_content(self.field_width,[])
            self.field_type=del_content(self.field_type,[])


    # for change the type to the platform unite
    def do_stats(self):
        for i in range(len(self.field_width)):
            self.reg_width.append(max(self.field_width[i])+1)#31:0 width 32bit
        for i in range(len(self.field_type)):
            if ("rw" in self.field_type[i]) or ("wr" in self.field_type[i]):
                self.reg_type.append("RW")#same as register
            elif ("r" in self.field_type[i]) and ("w" in self.field_type[i]):
                self.reg_type.append("RW")
            elif ("r" in self.field_type[i]) and ("w" not in self.field_type[i]):
                self.reg_type.append("R")
            elif ("r" not in self.field_type[i]) and ("w" in self.field_type[i]):
                self.reg_type.append("W")
            else:
                self.reg_type.append("RW")


# SystemRDL File----------------------------------> RDL class
#                      SystemRDL Compiler

class RDL(object):
    def __init__(self):
        self.files=[]#the RDL File
        self.rdlc=RDLCompiler()#for compiler the file 
        self.root="" #the file has been elaborate
        self.listener=GetRegListener()#using self listener

    #read rdl file
    @DEBUG()
    def read_rdl(self,files=[]):
        INFO("read_rdl: "+"Reading SystemRDL Files")
        try:
            #compile all the files provided
            for input_file in files:
                self.rdlc.compile_file(input_file)
            self.root=self.rdlc.elaborate()#get the root of  Tree in the RDL 
        except RDLCompileError:
            sys.exit(1)
        self.files=files
        walker = RDLWalker(unroll=True)
        walker.walk(self.root, self.listener)
        self.listener.do_stats()#to process the information of SystemRDL file

    #gen the html file according the SystemRDL file has been elaborate
    @DEBUG()
    def gen_html(self,outdir=""):
        #md=markdown.Markdown(extensions=['admonition'])
        INFO("gen_html: "+"Generate HTML File")
        md = markdown.Markdown()
        html=HTMLExporter(markdown_inst=md)
        html.export(self.root,outdir,home_url="")


    #gen the uvm file according the SystemRDL file has been elaborate
    @DEBUG()
    def gen_uvmral(self,outdir="",outfile=""):
        INFO("gen_uvmral: "+"Generate UVM-RAL File")
        exporter=uvmGenExporter()
        exporter.export(self.root,outdir,outfile)

    #gen the ip-xact file according the SystemRDL file has been elaborate
    @DEBUG()
    def gen_ipxact(self,outdir="",outfile=""):
        INFO("gen_ipxact: "+"Generate IP-XACT File")
        exporter=IPXACTExporter()
        exporter.export(self.root,outdir,outfile)


    def display_rdl(self):
        print(self.files)
        print(self.listener.reg_name)
        print(self.listener.reg_width)
        print(self.listener.reg_type)
        print(self.listener.reg_addr)
