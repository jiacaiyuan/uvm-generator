`ifndef {{ module.upper() }}_PKG_SV
`define {{ module.upper() }}_PKG_SV

`include "{{ module }}_defines.svh"
`include "{{ module }}_interface.svi"

package {{ module }}_pkg;
  import uvm_pkg::*;
  `include "uvm_macros.svh"

  `include "{{ module }}_type.sv"
  `include "{{ module }}_config.sv"
  `include "{{ module }}_item.sv"
  `include "{{ module }}_sequence_lib.sv"
  `include "{{ module }}_callbacks.sv"
  `include "{{ module }}_sequencer.sv"
  `include "{{ module }}_driver.sv"
  `include "{{ module }}_monitor.sv"
  `include "{{ module }}_analyzer.sv"
  `include "{{ module }}_collector.sv"
  `include "{{ module }}_adapter.sv"
  `include "{{ module }}_bus_checker.sv"
  `include "{{ module }}_agent.sv"
endpackage

`endif