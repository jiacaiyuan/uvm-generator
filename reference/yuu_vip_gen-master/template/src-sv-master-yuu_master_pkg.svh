`ifndef {{ module.upper() }}_MASTER_PKG_SVH
`define {{ module.upper() }}_MASTER_PKG_SVH

  `include "{{ module }}_master_config.sv"
  `include "{{ module }}_master_item.sv"
  `include "{{ module }}_master_sequence_lib.sv"
  `include "{{ module }}_master_callbacks.sv"
  `include "{{ module }}_master_sequencer.sv"
  `include "{{ module }}_master_driver.sv"
  `include "{{ module }}_master_monitor.sv"
  `include "{{ module }}_master_analyzer.sv"
  `include "{{ module }}_master_collector.sv"
  `include "{{ module }}_master_adapter.sv"
  `include "{{ module }}_master_agent.sv"

`endif