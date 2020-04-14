`ifndef {{ module.upper() }}_PKG_SV
`define {{ module.upper() }}_PKG_SV

`include "{{ module }}_defines.svh"
`include "{{ module }}_interface.svi"

package {{ module }}_pkg;
  import uvm_pkg::*;
  `include "uvm_macros.svh"

  `include "{{ module }}_common_pkg.svh"
  `include "{{ module }}_master_pkg.svh"
  `include "{{ module }}_slave_pkg.svh"
  `include "{{ module }}_env_pkg.svh"
endpackage

`endif