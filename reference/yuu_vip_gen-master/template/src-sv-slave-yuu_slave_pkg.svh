`ifndef {{ module.upper() }}_SLAVE_PKG_SVH
`define {{ module.upper() }}_SLAVE_PKG_SVH

  `include "{{ module }}_slave_config.sv"
  `include "{{ module }}_slave_item.sv"
  `include "{{ module }}_slave_sequence_lib.sv"
  `include "{{ module }}_slave_callbacks.sv"
  `include "{{ module }}_slave_sequencer.sv"
  `include "{{ module }}_slave_driver.sv"
  `include "{{ module }}_slave_monitor.sv"
  `include "{{ module }}_slave_analyzer.sv"
  `include "{{ module }}_slave_collector.sv"
  `include "{{ module }}_slave_agent.sv"

`endif