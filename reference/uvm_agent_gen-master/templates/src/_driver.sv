{% extends "_base.sv" %}

{% block body %}

class {{ agent.name }}_driver extends uvm_driver#({{ agent.name }}_item);
  `uvm_component_utils({{ agent.name }}_driver)

  // Config
  {{ agent.name }}_cfg  m_cfg;

  // Interface
  virtual {{ agent.name }}_if.drv_mp m_vif;

  // Analysis Port
  uvm_analysis_port#({{ agent.name }}_item) m_req_analysis_port;
  uvm_analysis_port#({{ agent.name }}_item) m_rsp_analysis_port;

  // Constructor
  function new (string name = "{{ agent.name }}_driver", uvm_component parent = null);
    super.new(name, parent);
  endfunction: new

  // Phase Methods
  extern virtual function void build_phase(uvm_phase phase);
  extern virtual function void connect_phase(uvm_phase phase);
  extern virtual task run_phase(uvm_phase phase);

  // Helper Methods
  extern virtual task drv_init();
  extern virtual task drv_interface();

endclass: {{ agent.name }}_driver

function void {{ agent.name }}_driver::build_phase(input uvm_phase phase);
  super.build_phase(phase);

  // Grab the Config
  if (!uvm_config_db#({{ agent.name }}_cfg)::get(this, "", "{{ agent.name }}_cfg", m_cfg)) begin
    `uvm_fatal(get_name(), "Failed to Grab {{ agent.name }}_cfg from Config DB")
  end

  // Build the Analysis Ports
  m_req_analysis_port = new("m_req_analysis_port", this);
  m_rsp_analysis_port = new("m_rsp_analysis_port", this);

endfunction: build_phase


function void {{ agent.name }}_driver::connect_phase(input uvm_phase phase);
  // Grab the Config
  if (!uvm_config_db#(virtual {{ agent.name }}_if.drv_mp)::get(this, "", "{{ agent.name }}_vif_drv", m_vif)) begin
    `uvm_fatal(get_name(), "Failed to Grab {{ agent.name }}_vif_drv from Config DB")
  end

endfunction: connect_phase

task {{ agent.name }}_driver::run_phase(uvm_phase phase);
  super.run_phase(phase);

  drv_init();

  fork
    drv_interface();
  join

endtask: run_phase

task {{ agent.name }}_driver::drv_init();

  // TODO: Initialize Interface - drive all outputs to inactive state
  // Example: m_vif.example_output_net = 0;
endtask: drv_init


task {{ agent.name }}_driver::drv_interface();

  forever begin
    // Get and item from the seq item port
    seq_item_port.get(req);
    m_req_analysis_port.write(req);

    // Construct Response
    rsp = RSP::type_id::create("rsp", this);

    // Copy Req ID to Rsp ID
    rsp.copy(req); // copy contents
    rsp.set_id_info(req); // copy sequence item id

    // TODO: implement driver code

    // Provide RSP to analysis port
    m_rsp_analysis_port.write(rsp);

    // Return Response to Sequence
    seq_item_port.put(rsp);

  end
endtask: drv_interface

{% endblock %}
