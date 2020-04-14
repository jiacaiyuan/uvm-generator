''' 2018/11/29 1.添加 frame_gen 逻辑用于方便的生成流输入 
               2.测试中存在丢失端口检测的情况     
               3.复位极性，时钟，复位信号无法自动检测
               4.信号没有再系统初始化的时候自动添加复位（reg型）
               
               添加 function blog2
                   function integer blog2(input integer num);
                        for ( blog2 = 0 ; num > 0 ; blog2 = blog2+1 )
                        num = num >> 1 ;
                    endfunction
    
    2018/12/3
                1.修复形如 input_cnt 等变量错误被识别为输入接口的BUG
                2.在gen_stream任务中添加tlast选项
                3.修复了初始化时数据与使能信号的清0
                4.添加复位逻辑将待测模块中属性为input端口全部置0
    
    2018/12/4
                1.添加工程文件夹模式，指定工程文件夹目录，目录中所有的
                文件都会被添加到测试空间的Verilog文件夹中
    2018/12/5
                1.将测试文档的生成编写成为一个函数，未后期的类化做准备
                2.对部分逻辑复杂代码进行优化
    
    2018/12/11  1.添加了读取用户输入的逻辑
                2.定位并解决了函数化后路径上的错误
                3.下一步预定添加信号绑定功能，用户可以通过命令行选择哪些
                信号作为总线中的时钟信号、复位信号、数据信号等
    
    2018/12/21  1.添加了类似于output reg signed [3:0] data;的支持，支持
                在端口声明reg类型
                2.添加将端口解析出来的多维列表转化为字典的函数，为后续功能优化
                提供基础
                3.修正了搜索参数定义的正则表达式，防止搜索到的参数值包含换行符
                4.将程序中原有通过正则表达式搜索的多维列表全部改为字典，并修改
                了程序中的其他接口
    2019/1/31   1.发现了不能正确识别 output reg[DW*WL-1:0]   m_axis_tdata 类型
                信号，因为reg与后端[符号并未添加多余空格，问题待解决
    
    2019/08/08  1.修正不能正确识别如parameter P = {16{1'b1}} ; 等形式参数的错误
    '''
    
''' This Program is Used to Create TestBench For a Verilog File '''
import os 
import shutil
import time
import re
import pickle
import sys



## Regex Function Get & Delete
format_get = lambda format,string : re.compile(format).findall(string)
format_delete = lambda format,string : re.compile(format).sub('',string)

## This Function Convert List to Dictionary
list2dict=lambda keys,vals : [ dict(zip(keys,item)) for item in vals]


    

    
def testbench_analyze(dut_fid):
    ''' 分析Verilog代码并产生对应的测试文本 '''
    ''' 未考虑到函数里的端口定义，与线网 signed情况 '''
    #print_info('Start Verilog File Analyze!')
    file=dut_fid.read()
    
    # 去除所有注释部分 
    file=format_delete('(/{2,}.*?\n)|(?:/\*(\n|.)*?\*/)',file)

    # 模块名位于'module'后，若有参数列表则位于'#'前，否则则位于'('前
    #module_name=format_get('module\s*(\S*)\s*[#|\(]',file)[0]
    module_name=format_get('module\s*(\S*)\s*[#|\(]',file)[0]
    #print('Module Name Table : \n')
    #print_table(['Name'],module_name)
    
    # 提取参数列表中的参数 提取逻辑可以表示如下 位于#右侧的第一个括号内以,分割
    param_info=format_get('((?:parameter)|(?:localparam))\s*(\w*)\s*=\s*(.*?)\s*[;,)]',file)
    #print('Parameter Information Table  :')
    #print_table(['Type','Name','Value'],param_info)
    param_dict=list2dict(['Type','Name','Value'],param_info)
    
    # 提取端口具体信息
    file=format_delete('(?:function)(?:.|\n)*(?:endfunction)',file)# 提前删除function->endfunction防止function中有端口声明
    port_info = format_get('((?:input)|(?:output)|(?:inout))(?:\s+(?:(?:reg)|(?:wire)))?\s+((?:signed)|(?:unsigned))?\s*(?:\[\s*(\S*)\s*:\s*(\S*)\s*\])?\s*(\w*)(?:\n|.)*?[;,)]',file)
    #print('Port Information Table  :')
    #print_table(['IO Type','SIGNED','MSB','LSB','Name'],port_info)
    port_dict=list2dict(['IO Type','SIGNED','MSB','LSB','Name'],port_info)
    
    # 生成例化原型
    return ( module_name , param_dict , port_dict)
    
    

def testbench_file_generate(fil):
    ''' 产生testbench文件 '''
    ## Analyze the Top Module And Gernerate the Test Bench
    dut_fid     = open(fil,'r')
    module_name , param_dict , port_dict=testbench_analyze(dut_fid)
    print(module_name)
    print(param_dict)
    print(port_dict)


testbench_file_generate(sys.argv[1])