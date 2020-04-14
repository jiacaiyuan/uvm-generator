`ifndef {{ module.upper() }}_ITEM_SV
`define {{ module.upper() }}_ITEM_SV

class {{ module }}_item extends uvm_sequence_item;
  // Data members
  {{ module }}_config cfg;

  // Constraints

  `uvm_object_utils_begin({{ module }}_item)
  `uvm_object_utils_end

  // Function declarations
  extern function      new(string name="{{ module }}_item");
  extern function void pre_randomize();
endclass

function {{ module }}_item::new(string name="{{ module }}_item");
  super.new(name);
endfunction

function void {{ module }}_item::pre_randomize();
  super.pre_randomize();

  if (!uvm_config_db #({{ module }}_config)::get(null, get_full_name(), "cfg", cfg) && cfg == null)
    `uvm_fatal("pre_randomize", "Cannot get {{ module.upper() }} configuration in transaction")
endfunction

`endif