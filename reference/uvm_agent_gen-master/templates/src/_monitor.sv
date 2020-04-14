{% extends "_base.sv" %}

{% block body %}

class {{ agent.name }}_monitor extends uvm_monitor;
  `uvm_component_utils({{ agent.name }}_monitor)

  // Config
  {{ agent.name }}_cfg  m_cfg;

  // Interface
  virtual {{ agent.name }}_if.mon_mp m_vif;

  // Analysis Port
  uvm_analysis_port#({{ agent.name }}_item) m_analysis_port;

  // Constructor
  function new (string name = "{{ agent.name }}_monitor", uvm_component parent = null);
    super.new(name, parent);
  endfunction: new

  // Phase Methods
  extern virtual function void build_phase(uvm_phase phase);
  extern virtual function void connect_phase(uvm_phase phase);
  extern virtual task run_phase(uvm_phase phase);

  // Helper Methods
  extern virtual task mon_interface();

endclass: {{ agent.name }}_monitor


function void {{ agent.name }}_monitor::build_phase(input uvm_phase phase);
  super.build_phase(phase);

  // Grab the Config
  if (!uvm_config_db#({{ agent.name }}_cfg)::get(this, "", "{{ agent.name }}_cfg", m_cfg)) begin
    `uvm_fatal(get_name(), "Failed to Grab {{ agent.name }}_cfg from Config DB")
  end

  // Build the Analysis Ports
  m_analysis_port = new("m_analysis_port", this);

endfunction: build_phase


function void {{ agent.name }}_monitor::connect_phase(input uvm_phase phase);
  // Grab the Config
  if (!uvm_config_db#(virtual {{ agent.name }}_if.mon_mp)::get(this, "", "{{ agent.name }}_vif_mon", m_vif)) begin
    `uvm_fatal(get_name(), "Failed to Grab {{ agent.name }}_vif_mon from Config DB")
  end

endfunction: connect_phase

task {{ agent.name }}_monitor::run_phase(uvm_phase phase);
  super.run_phase(phase);

  fork
    mon_interface();
  join

endtask: run_phase

task {{ agent.name }}_monitor::mon_interface();
  {{ agent.name }}_item mon_item_h;

  forever begin

    // Wait for a valid access
    @(m_vif.mon_cb);

    // TODO: monitor interface for transaction

    // Construct Monitored Item
    mon_item_h = {{ agent.name }}_item::type_id::create("mon_item", this);

    // TODO: assemble the mon_item here

    // Write the Item out
    m_analysis_port.write(mon_item_h);

  end

endtask: mon_interface

{% endblock %}
