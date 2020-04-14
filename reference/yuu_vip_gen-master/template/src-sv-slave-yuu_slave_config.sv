`ifndef {{ module.upper() }}_SLAVE_CONFIG_SV
`define {{ module.upper() }}_SLAVE_CONFIG_SV

class {{ module }}_slave_config extends {{ module }}_agent_config;
  // Data members
  virtual {{ module }}_slave_interface  vif;
  
  // Constraints

  `uvm_object_utils_begin({{ module }}_slave_config)
  `uvm_object_utils_end

  // Function declarations
  extern function new(string name="{{ module }}_slave_config");
endclass

function {{ module }}_slave_config::new(string name="{{ module }}_slave_config");
  super.new(name);
endfunction

`endif