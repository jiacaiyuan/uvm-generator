`timescale 1ns/1ps
package dut_pkg;

import uvm_pkg::*;
`include "uvm_macros.svh"

`include "dut_sequence_cfg.sv"
`include "dut_env_cfg.sv"

`include "bus_transaction.sv"
`include "bus_agent_cfg.sv"
`include "bus_sequencer.sv"
`include "bus_driver.sv"
`include "bus_monitor.sv"
`include "bus_agent.sv"
`include "bus_reg_adapter.sv"
`include "bus_sequence_base.sv"



`include "slave_transaction.sv"
`include "slave_agent_cfg.sv"
`include "slave_sequencer.sv"
`include "slave_driver.sv"
`include "slave_monitor.sv"
`include "slave_agent.sv"
`include "slave_sequence_base.sv"



`include "master_transaction.sv"
`include "master_agent_cfg.sv"
`include "master_sequencer.sv"
`include "master_driver.sv"
`include "master_monitor.sv"
`include "master_agent.sv"
`include "master_sequence_base.sv"


`include "UART_uvm.sv"


`include "dut_virtual_sequencer.sv"
`include "dut_env.sv"
`include "dut_base_test.sv"

endpackage


