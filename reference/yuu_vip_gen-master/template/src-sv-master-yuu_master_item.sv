`ifndef {{ module.upper() }}_MASTER_ITEM_SV
`define {{ module.upper() }}_MASTER_ITEM_SV

class {{ module }}_master_item extends {{ module }}_item;
  // Data members
  {{ module }}_master_config cfg;

  // Constraints

  `uvm_object_utils_begin({{ module }}_master_item)
  `uvm_object_utils_end

  // Function declarations
  extern function      new(string name="{{ module }}_master_item");
  extern function void pre_randomize();
endclass

function {{ module }}_master_item::new(string name="{{ module }}_master_item");
  super.new(name);
endfunction

function void {{ module }}_master_item::pre_randomize();
  super.pre_randomize();

  if (!uvm_config_db #({{ module }}_master_config)::get(null, get_full_name(), "cfg", cfg) && cfg == null)
    `uvm_fatal("pre_randomize", "Cannot get {{ module.upper() }} master configuration in transaction")
endfunction

`endif