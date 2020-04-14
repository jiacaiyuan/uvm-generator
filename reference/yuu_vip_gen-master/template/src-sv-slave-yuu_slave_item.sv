`ifndef {{ module.upper() }}_SLAVE_ITEM_SV
`define {{ module.upper() }}_SLAVE_ITEM_SV

class {{ module }}_slave_item extends {{ module }}_item;
  // Data members
  {{ module }}_slave_config cfg;

  // Constraints

  `uvm_object_utils_begin({{ module }}_slave_item)
  `uvm_object_utils_end

  // Function declarations
  extern function      new(string name="{{ module }}_slave_item");
  extern function void pre_randomize();
endclass

function {{ module }}_slave_item::new(string name="{{ module }}_slave_item");
  super.new(name);
endfunction

function void {{ module }}_slave_item::pre_randomize();
  super.pre_randomize();

  if (!uvm_config_db #({{ module }}_slave_config)::get(null, get_full_name(), "cfg", cfg) && cfg == null)
    `uvm_fatal("pre_randomize", "Cannot get {{ module.upper() }} slave configuration in transaction")
endfunction

`endif