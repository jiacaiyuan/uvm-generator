{% extends "_base.sv" %}

{% block body %}
// Sequence List - Lists available sequences of the {{agent.name}} Agent
`include "{{ agent.name }}_nominal_seq.sv"

{% endblock %}
