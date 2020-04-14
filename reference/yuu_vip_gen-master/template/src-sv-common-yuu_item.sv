`ifndef {{ module.upper() }}_ITEM_SVH
`define {{ module.upper() }}_ITEM_SVH

class {{ module }}_item extends uvm_sequence_item;
  // Data members

  // Constraints

  `uvm_object_utils_begin({{ module }}_item)
  `uvm_object_utils_end
  
  // Function declarations
  extern function new(string name="{{ module }}_item");
endclass

function {{ module }}_item::new(string name="{{ module }}_item");
  super.new(name);
endfunction

`endif