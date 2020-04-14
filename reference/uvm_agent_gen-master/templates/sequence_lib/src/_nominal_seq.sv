{% extends "_base.sv" %}

{% block body %}

// Nominal Seq -- just a wrapper for the item / driver interaction
//  simplifies the user api from start, finish, rand, get to just start
class {{ agent.name }}_nominal_seq extends uvm_sequence#({{ agent.name }}_item);
  `uvm_object_utils({{ agent.name }}_nominal_seq)

  // Members
  // TODO: implement rand and state members - members should match {{ agent.name }}_item
  // Example: rand int m_data;
  // Example: int m_rdata;

  // Constraints
  // TODO: implement constraints - should match the constraints in {{ agent.name }}_item

  // Constructor
  function new(string name = "{{ agent.name }}_nominal_seq");
    super.new(name);
  endfunction: new

  // Sequence Body
  extern virtual task body();

endclass: {{ agent.name }}_nominal_seq

task {{ agent.name }}_nominal_seq::body();

  req = REQ::type_id::create("req", null, get_full_name());

  start_item(req);

  if (!req.randomize() with {
    // TODO: Constrain item with local rand variables
    // Example: m_data == local::m_data;
  }) begin
    `uvm_fatal(get_name(), "randomize failed")
  end

  finish_item(req);

  get_response(rsp);

  // TODO: grab any response data here
  //  Example: m_read_data = rsp.rdata;

endtask: body

{% endblock %}
