`ifndef {{ module.upper() }}_MASTER_CONFIG_SV
`define {{ module.upper() }}_MASTER_CONFIG_SV

class {{ module }}_master_config extends {{ module }}_agent_config;
  // Data members
  virtual {{ module }}_master_interface  vif;

  boolean use_reg_model = False;
  
  // Constraints

  `uvm_object_utils_begin({{ module }}_master_config)
    `uvm_field_enum(boolean, use_reg_model, UVM_PRINT | UVM_COPY)
  `uvm_object_utils_end

  // Function declarations
  extern function new(string name="{{ module }}_master_config");
endclass

function {{ module }}_master_config::new(string name="{{ module }}_master_config");
  super.new(name);
endfunction

`endif