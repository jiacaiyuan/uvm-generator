#!/usr/bin/env python3
###################################################################################
# Copyright 2020 seabeam@yahoo.com - Licensed under the Apache License, Version 2.0
# For more information, see LICENCE in the main folder
###################################################################################
import os
import shutil
import argparse

from jinja2 import Environment, FileSystemLoader

agent_list = [
    "include-yuu_defines.svh",
    "src-sv-agent-yuu_adapter.sv",
    "src-sv-agent-yuu_agent.sv",
    "src-sv-agent-yuu_analyzer.sv",
    "src-sv-agent-yuu_bus_checker.sv",
    "src-sv-agent-yuu_callbacks.sv",
    "src-sv-agent-yuu_collector.sv",
    "src-sv-agent-yuu_config.sv",
    "src-sv-agent-yuu_driver.sv",
    "src-sv-agent-yuu_interface.svi",
    "src-sv-agent-yuu_item.sv",
    "src-sv-agent-yuu_monitor.sv",
    "src-sv-agent-yuu_pkg.sv",
    "src-sv-agent-yuu_sequence_lib.sv",
    "src-sv-agent-yuu_sequencer.sv",
    "src-sv-agent-yuu_type.sv",
]

env_list = [
    "include-yuu_defines.svh",
    "include-yuu_interface.svi",
    "include-yuu_pkg.sv",
    "src-sv-common-yuu_agent_config.sv",
    "src-sv-common-yuu_common_pkg.svh",
    "src-sv-common-yuu_item.sv",
    "src-sv-common-yuu_type.sv",
    "src-sv-env-yuu_env_checker.sv",
    "src-sv-env-yuu_env_config.sv",
    "src-sv-env-yuu_env_pkg.svh",
    "src-sv-env-yuu_env.sv",
    "src-sv-env-yuu_virtual_sequencer.sv",
    "src-sv-master-yuu_master_adapter.sv",
    "src-sv-master-yuu_master_agent.sv",
    "src-sv-master-yuu_master_analyzer.sv",
    "src-sv-master-yuu_master_callbacks.sv",
    "src-sv-master-yuu_master_collector.sv",
    "src-sv-master-yuu_master_config.sv",
    "src-sv-master-yuu_master_driver.sv",
    "src-sv-master-yuu_master_interface.svi",
    "src-sv-master-yuu_master_item.sv",
    "src-sv-master-yuu_master_monitor.sv",
    "src-sv-master-yuu_master_pkg.svh",
    "src-sv-master-yuu_master_sequence_lib.sv",
    "src-sv-master-yuu_master_sequencer.sv",
    "src-sv-slave-yuu_slave_agent.sv",
    "src-sv-slave-yuu_slave_analyzer.sv",
    "src-sv-slave-yuu_slave_callbacks.sv",
    "src-sv-slave-yuu_slave_collector.sv",
    "src-sv-slave-yuu_slave_config.sv",
    "src-sv-slave-yuu_slave_driver.sv",
    "src-sv-slave-yuu_slave_interface.svi",
    "src-sv-slave-yuu_slave_item.sv",
    "src-sv-slave-yuu_slave_monitor.sv",
    "src-sv-slave-yuu_slave_pkg.svh",
    "src-sv-slave-yuu_slave_sequence_lib.sv",
    "src-sv-slave-yuu_slave_sequencer.sv",
]

def parse_file(filename, module):
    l = filename.split('-')
    if len(l) > 2:
        l[-2] = module + '_' + l[-2]
    path = '/'.join(l[:len(l)-1])
    file = l[-1].replace('yuu', module)
    return (path, file) 

if __name__  == '__main__':
    arg_parser = argparse.ArgumentParser(description="VIP template generation autimatic")
    arg_parser.add_argument('-m', '--module', required=True, help='[Required] Expected module name')
    arg_parser.add_argument('-p', '--prefix', required=False, help='[Optional] Module prefix')
    arg_parser.add_argument('-o', '--output', required=False, default="./", help='[Optional] Output path')
    arg_parser.add_argument('-e', '--env', required=False, action="store_true", help='[Optional] Including master/slave/environment')
    arg_parser.add_argument('--addr_width', required=False, type=int, default=0, help='[Optional] Transaction address width')
    arg_parser.add_argument('--data_width', required=False, type=int, default=0, help='[Optional] Transaction data width')
    args = arg_parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = '%s/template' %(script_dir)
    env = Environment(loader=FileSystemLoader(template_dir))

    if args.prefix != None:
        module_name = args.prefix + '_' + args.module
    else:
        module_name = args.module
    
    if args.addr_width <= 0:
        aw = 32
    else:
        aw = args.addr_width

    if args.data_width <= 0:
        dw = 32
    else:
        dw = args.data_width

    shutil.rmtree('%s/include' %(args.output), ignore_errors=True)
    shutil.rmtree('%s/src' %(args.output), ignore_errors=True)
    shutil.rmtree('%s/test' %(args.output), ignore_errors=True)
    shutil.rmtree('%s/sim' %(args.output), ignore_errors=True)

    if args.env:
        for item in env_list:
            (path, file) = parse_file(item, module_name)
            try:
                os.makedirs('%s/%s' %(args.output, path))
            except FileExistsError:
                pass
            template = env.get_template(item)
            with open('%s/%s/%s' %(args.output, path, file), 'w', encoding='UTF-8') as f:
                f.write(template.render(module=module_name, use_env=args.env, addr_width=aw, data_width=dw))
    else:
        for item in agent_list:
            (path, file) = parse_file(item, module_name)
            try:
                os.makedirs('%s/%s' %(args.output, path))
            except FileExistsError:
                pass
            template = env.get_template(item)
            with open('%s/%s/%s' %(args.output, path, file), 'w', encoding='UTF-8') as f:
                f.write(template.render(module=module_name, use_env=args.env, addr_width=aw, data_width=dw))

        shutil.move('%s/src/sv/%s_agent/%s_interface.svi' %(args.output, module_name, module_name), '%s/include' %(args.output))
        shutil.move('%s/src/sv/%s_agent/%s_pkg.sv' %(args.output, module_name, module_name), '%s/include' %(args.output))
    
    os.mkdir('%s/test' %(args.output))
    os.mkdir('%s/sim' %(args.output))
    os.mkdir('%s/src/c' %(args.output))
    os.mkdir('%s/src/dpi' %(args.output))

    print('VIP %s template generation done in path %s' %(module_name, args.output))