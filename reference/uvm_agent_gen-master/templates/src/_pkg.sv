{% extends "_base.sv" %}

{% block body %}

`include "uvm_macros.svh"
import uvm_pkg::*;

package {{ agent.name }}_pkg;

  // Custom Types

  // Include the Agent files
  `include "{{ agent.name }}_item.sv"
  `include "{{ agent.name }}_cfg.sv"
  `include "{{ agent.name }}_sequencer.sv"
  `include "{{ agent.name }}_driver.sv"
  `include "{{ agent.name }}_monitor.sv"
  `include "{{ agent.name }}_agent.sv"
  `include "{{ agent.name }}_sequence_list.sv"

endpackage: {{ agent.name }}_pkg

{% endblock %}
