#!/usr/bin/env python

import os
import sys
import shutil
import json
from mako.template import Template
from mako.lookup import TemplateLookup

if len(sys.argv) == 2:
    conf_file = sys.argv[1]
else:
    conf_file = "config.json"

print('uvm agent generator 1.0')
print('')

# set template path
template_path = os.getcwd() + os.sep + 'template_agent'
mylookup = TemplateLookup(directories=[template_path], module_directory='/tmp/mako_modules')
print('TEMPLATE DIR: ' + template_path)
print('')

# get agent parameters from config.json
f = open(conf_file, 'r')
conf = json.load(f)
agent_name = conf['agent_name']
itf = conf['itf']
seq_name = conf['seq_name']
f.close()
print('Current Configuration:')
print('  agent name: ' + agent_name)
print('  interface: ' + ','.join(itf))
print('  seq name:' + seq_name)
print('')

# create agent directory
agent_dir = agent_name + '_agent'
if os.path.exists(agent_dir):
    shutil.rmtree(agent_dir)
os.mkdir(agent_dir)
print('RESULT DIR: ' + agent_dir)
print('')

# define template handle function
def uvm_file_gen(filename, **kwargs):
    uvm_template = mylookup.get_template(filename)
    fd = open(agent_dir + os.sep + filename.replace('template', agent_name), 'w')
    fd.write(uvm_template.render(**kwargs))
    fd.close()
    print('Generating ' + agent_dir + os.sep + filename.replace('template', agent_name))

# template rendering
uvm_file_gen('template_agent_pkg.sv', agent_name=agent_name, itf=itf, seq_name=seq_name)
uvm_file_gen('template_agent.svh', agent_name=agent_name, itf=itf, seq_name=seq_name)
uvm_file_gen('template_agent_cfg.svh', agent_name=agent_name, itf=itf, seq_name=seq_name)
uvm_file_gen('template_driver.svh', agent_name=agent_name, itf=itf, seq_name=seq_name)
uvm_file_gen('template_monitor.svh', agent_name=agent_name, itf=itf, seq_name=seq_name)
uvm_file_gen('template_sequencer.svh', agent_name=agent_name, itf=itf, seq_name=seq_name)

