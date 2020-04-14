{% extends "_base.sv" %}

{% block body %}

class {{ agent.name }}_item extends uvm_sequence_item;

  // Members
  // TODO: implement rand members
  // Example: rand int m_data;
  // Example: int m_rdata;

  // Constraints
  // TODO: implement constraints

  // Constructor
  function new (string name = "{{ agent.name }}_item");
    super.new(name);
  endfunction: new

  // Field Macros
  `uvm_object_utils_begin({{ agent.name }}_item)
    // UVM Field macros...
    // TODO: implement field macros
    // Example: `uvm_field_int(m_data, UVM_ALL_ON)
  `uvm_object_utils_end


endclass: {{ agent.name }}_item

{% endblock %}
