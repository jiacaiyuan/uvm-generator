#! /usr/bin/env python

'''
vTbgenerator.py -- generate verilog module Testbench
generated bench file like this:

        fifo_sc #(
            .DATA_WIDTH ( 8 ),
            .ADDR_WIDTH ( 8 )
        )
         u_fifo_sc (
            .CLK   ( CLK                     ),
            .RST_N ( RST_N                   ),
            .RD_EN ( RD_EN                   ),
            .WR_EN ( WR_EN                   ),
            .DIN   ( DIN   [DATA_WIDTH-1 :0] ),
            .DOUT  ( DOUT  [DATA_WIDTH-1 :0] ),
            .EMPTY ( EMPTY                   ),
            .FULL  ( FULL                    )
        );

Usage:
      python vTbgenerator.py ModuleFileName.v

'''
import random
import re
import sys
from queue import Queue

import chardet


def delComment(Text):
    """ removed comment """
    single_line_comment = re.compile(r"//(.*)$", re.MULTILINE)
    multi_line_comment = re.compile(r"/\*(.*?)\*/", re.DOTALL)
    Text = multi_line_comment.sub('\n', Text)
    Text = single_line_comment.sub('\n', Text)
    return Text


def delBlock(Text):
    """ removed task and function block """
    Text = re.sub(r'\Wtask\W[\W\w]*?\Wendtask\W', '\n', Text)
    Text = re.sub(r'\Wfunction\W[\W\w]*?\Wendfunction\W', '\n', Text)
    return Text


def findName(inText):
    """ find module name and port list"""
    p = re.search(r'([a-zA-Z_][a-zA-Z_0-9]*)\s*', inText)
    mo_Name = p.group(0).strip()
    return mo_Name


def paraDeclare(inText, portArr):
    """ find parameter declare """
    pat = r'\s' + portArr + r'\s[\w\W]*?[;,)]'
    ParaList = re.findall(pat, inText)

    return ParaList


def portDeclare(inText, portArr):
    """find port declare, Syntax:
       input [ net_type ] [ signed ] [ range ] list_of_port_identifiers

       return list as : (port, [range])
    """
    port_definition = re.compile(
        r'\b' + portArr +
        r''' (\s+(wire|reg)\s+)* (\s*signed\s+)*  (\s*\[.*?:.*?\]\s*)*
        (?P<port_list>.*?)
        (?= \binput\b | \boutput\b | \binout\b | ; | \) )
        ''',
        re.VERBOSE | re.MULTILINE | re.DOTALL
    )

    pList = port_definition.findall(inText)
    t = []
    for ls in pList:
        if len(ls) >= 2:
            t = t + portDic(ls[-2:])
    return t


def portDic(port):
    """delet as : input a =c &d;
        return list as : (port, [range])
    """
    pRe = re.compile(r'(.*?)\s*=.*', re.DOTALL)

    pRange = port[0]
    pList = port[1].split(',')
    pList = [i.strip() for i in pList if i.strip() != '']
    pList = [(pRe.sub(r'\1', p), pRange.strip()) for p in pList]

    return pList


def formatPort(AllPortList, isPortRange=1):
    PortList = AllPortList

    str = ''
    if PortList != []:
        l1 = max([len(i[0]) for i in PortList])+2
        l3 = max(18, l1)

        strList = []
        str = ',\n'.join([' ' * 4 + '.' + i[0].ljust(l3)
                          + '(' + (i[0]) + ')' for i in AllPortList])
        strList = strList + [str]

        str = ',\n\n'.join(strList)

    return str


def formatDeclare(PortList, portArr, initial=""):
    str = ''

    if PortList != []:
        str = '\n'.join([portArr.ljust(4) + '  '+(i[1]+min(len(i[1]), 1)*'  '
                                                  + i[0]) + ';' for i in PortList])
    return str


def formatPara(ParaList):
    paraDec = ''
    paraDef = ''
    if ParaList != []:
        s = '\n'.join(ParaList)
        pat = r'([a-zA-Z_][a-zA-Z_0-9]*)\s*=\s*([\w\W]*?)\s*[;,)]'
        p = re.findall(pat, s)

        l1 = max([len(i[0]) for i in p])
        l2 = max([len(i[1]) for i in p])
        paraDec = '\n'.join(['parameter %s = %s;'
                             % (i[0].ljust(l1 + 1), i[1].ljust(l2))
                             for i in p])
        paraDef = '#(\n' + ',\n'.join(['    .' + i[0].ljust(l1 + 1)
                                       + '( ' + i[1].ljust(l2)+' )' for i in p]) + ')\n'
    return paraDec, paraDef


def portT(inText, ioPadAttr):
    x = {}
    count_list = []
    order_list = []
    for i in ioPadAttr:
        p = port_index_list(inText, i)
        for j in p:
            count_list.append(j)
            x[j] = i
    count_list = quick_sort(count_list, 0, len(count_list)-1)
    for c in count_list:
        order_list.append(x.get(c))
    return order_list


def quick_sort(myList, start, end):
    if start < end:
        i, j = start, end
        base = myList[i]
        while i < j:
            while (i < j) and (myList[j] >= base):
                j = j - 1

            myList[i] = myList[j]

            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        myList[i] = base

        quick_sort(myList, start, i - 1)
        quick_sort(myList, j + 1, end)
    return myList


def formatPort_order(padAttr, orderList):

    for p in padAttr:
        q = Queue()
        for i in padAttr.get(p):
            q.put(i)
        padAttr[p] = q
    AllPortList = []
    for o in orderList:
        AllPortList.append(padAttr.get(o).get())
    return AllPortList


def port_index_list(intext, text):
    l = []
    t = intext
    index = t.find(text)
    while index > -1:
        t = t.replace(text, random_str(len(text)), 1)
        l.append(index)
        index = t.find(text)
    return l


def random_str(size):
    s = ''
    for i in range(size):
        s += str(random.randint(0, 9))
    return s


def getPortMap(AllPortList, ioPadAttr):
    if len(AllPortList) != len(ioPadAttr):
        return

    p_map = {}
    for i in range(len(AllPortList)):
        p_map[ioPadAttr[i]] = AllPortList[i]
    return p_map


def writeTestBench(input_file):
    """ write testbench to file """
    with open(input_file, 'rb') as f:
        f_info = chardet.detect(f.read())
        f_encoding = f_info['encoding']
    with open(input_file, encoding=f_encoding) as inFile:
        inText = inFile.read()

    # removed comment,task,function
    inText = delComment(inText)
    inText = delBlock(inText)

    # moduel ... endmodule  #
    moPos_begin = re.search(r'(\b|^)module\b', inText).end()
    moPos_end = re.search(r'\bendmodule\b', inText).start()
    inText = inText[moPos_begin:moPos_end]

    name = findName(inText)
    paraList = paraDeclare(inText, 'parameter')
    paraDec, paraDef = formatPara(paraList)

    ioPadAttr = ['input', 'output', 'inout']
    orlder = portT(inText, ioPadAttr)
    input = portDeclare(inText, ioPadAttr[0])
    output = portDeclare(inText, ioPadAttr[1])
    inout = portDeclare(inText, ioPadAttr[2])

    portList = formatPort(formatPort_order(
        getPortMap([input, output, inout], ioPadAttr), orlder))

    input = formatDeclare(input, 'reg')
    output = formatDeclare(output, 'wire')
    inout = formatDeclare(inout, 'wire')

    # write Instance

    # module_parameter_port_list
    if(paraDec != ''):
        print("// %s Parameters\n%s\n" % (name, paraDec))

    # list_of_port_declarations
    #print("// %s Inputs\n%s\n" % (name, input))
    #print("// %s Outputs\n%s\n" % (name, output))
    #if(inout != ''):
    #    print("// %s Bidirs\n%s\n" % (name, inout))
    print("\n")
    # UUT
    print("%s %s inst_%s (\n%s\n);" % (name, paraDef, name, portList))


if __name__ == '__main__':
     writeTestBench(sys.argv[1])