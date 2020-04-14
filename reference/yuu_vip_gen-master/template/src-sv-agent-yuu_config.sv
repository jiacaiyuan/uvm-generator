`ifndef {{ module.upper() }}_CONFIG_SV
`define {{ module.upper() }}_CONFIG_SV

class {{ module }}_config extends uvm_object;
  // Data members
  virtual {{ module }}_interface  vif;

  uvm_event_pool events;
  int unsigned  addr_width = `{{ module.upper() }}_ADDR_WIDTH;
  int unsigned  data_width = `{{ module.upper() }}_DATA_WIDTH;
  int           timeout = 0;
  uvm_active_passive_enum is_active = UVM_ACTIVE;

  boolean use_reg_model = False;
  boolean analysis_enable = False;
  boolean coverage_enable = False;
  boolean protocol_check_enable = True;
  
  // Constraints

  `uvm_object_utils_begin({{ module }}_config)
    `uvm_field_int (                          addr_width,             UVM_PRINT | UVM_COPY)
    `uvm_field_int (                          data_width,             UVM_PRINT | UVM_COPY)
    `uvm_field_int (                          timeout,                UVM_PRINT | UVM_COPY)
    `uvm_field_enum(uvm_active_passive_enum,  is_active,              UVM_PRINT | UVM_COPY)
    `uvm_field_enum(boolean,                  coverage_enable,        UVM_PRINT | UVM_COPY)
    `uvm_field_enum(boolean,                  analysis_enable,        UVM_PRINT | UVM_COPY)
    `uvm_field_enum(boolean,                  protocol_check_enable,  UVM_PRINT | UVM_COPY)
    `uvm_field_enum(boolean,                  use_reg_model,          UVM_PRINT | UVM_COPY)
  `uvm_object_utils_end

  // Function declarations
  extern function new(string name="{{ module }}_config");
endclass

function {{ module }}_config::new(string name="{{ module }}_config");
  super.new(name);
endfunction

`endif