{% extends "_base.sv" %}

{% block body %}

class {{ agent.name }}_sequencer extends uvm_sequencer#({{ agent.name }}_item);
  `uvm_component_utils({{ agent.name }}_sequencer)

  // Constructor
  function new (string name = "{{ agent.name }}_sequencer", uvm_component parent = null);
    super.new(name, parent);
  endfunction: new

endclass: {{ agent.name }}_sequencer

{% endblock %}
