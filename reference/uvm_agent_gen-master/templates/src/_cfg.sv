{% extends "_base.sv" %}

{% block body %}

class {{ agent.name }}_cfg extends uvm_object;

  // Member Variables to define how the Host Agent is to be built
  uvm_active_passive_enum m_uvm_active_passive_h;
  // TODO: implement additional member variables used to configure the {{ agent.name }} agent

  // Constructor
  function new (string name = "{{ agent.name }}_cfg");
    super.new(name);
  endfunction: new

  // Field Macros
  `uvm_object_utils_begin({{ agent.name }}_cfg)
    `uvm_field_enum(uvm_active_passive_enum, m_uvm_active_passive_h, UVM_ALL_ON)
  `uvm_object_utils_end

endclass: {{ agent.name }}_cfg

{% endblock %}
