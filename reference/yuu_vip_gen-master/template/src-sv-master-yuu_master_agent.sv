`ifndef {{ module.upper() }}_MASTER_AGENT_SV
`define {{ module.upper() }}_MASTER_AGENT_SV

class {{ module }}_master_agent extends uvm_agent;
  // Data members
  {{ module }}_master_config  cfg;

  {{ module }}_master_sequencer  sequencer;
  {{ module }}_master_driver     driver;
  {{ module }}_master_monitor    monitor;
  {{ module }}_master_collector  collector;
  {{ module }}_master_analyzer   analyzer;
  {{ module }}_master_adapter    adapter;
  {{ module }}_master_predictor  predictor;

  uvm_analysis_port #({{ module }}_master_item) out_driver_ap;
  uvm_analysis_port #({{ module }}_master_item) out_monitor_ap;

  `uvm_component_utils_begin({{ module }}_master_agent)
  `uvm_component_utils_end

  // Function declarations
  extern         function      new(string name, uvm_component parent);
  extern virtual function void build_phase(uvm_phase phase);
  extern virtual function void connect_phase(uvm_phase phase);
  extern virtual function void end_of_elaboration_phase(uvm_phase phase);
endclass

function {{ module }}_master_agent::new(string name, uvm_component parent);
  super.new(name, parent);
endfunction

function void {{ module }}_master_agent::build_phase(uvm_phase phase);
  if (!uvm_config_db #({{ module }}_master_config)::get(null, get_full_name(), "cfg", cfg)) begin
    `uvm_fatal("build_phase", "Cannot get {{ module }} master configuration");
  end
  if (cfg == null)
    `uvm_fatal("build_phase", "Get a null {{ module }} master configuration")

  monitor = {{ module }}_master_monitor::type_id::create("monitor", this);
  monitor.cfg = cfg;
  if (cfg.is_active == UVM_ACTIVE) begin
    sequencer = {{ module }}_master_sequencer::type_id::create("sequencer", this);
    driver = {{ module }}_master_driver::type_id::create("driver", this);
    sequencer.cfg = cfg;
    driver.cfg = cfg;
  end
  if (cfg.coverage_enable) begin
    collector = {{ module }}_master_collector::type_id::create("collector", this);
    collector.cfg = cfg;
  end
  if (cfg.analysis_enable) begin
    analyzer = {{ module }}_master_analyzer::type_id::create("analyzer", this);
    analyzer.cfg = cfg;
  end

  if (cfg.use_reg_model) begin
    adapter = {{ module }}_master_adapter::type_id::create("adapter");
    adapter.cfg = cfg;
    adapter.provides_responses = 1;

    predictor = {{ module }}_master_predictor::type_id::create("predictor", this);
    predictor.adapter = adapter;
  end
endfunction

function void {{ module }}_master_agent::connect_phase(uvm_phase phase);
  out_monitor_ap = monitor.out_monitor_ap;

  if (cfg.is_active == UVM_ACTIVE) begin
    driver.seq_item_port.connect(sequencer.seq_item_export);
    out_driver_ap = driver.out_driver_ap;
  end
  if (cfg.coverage_enable) begin
    monitor.out_monitor_ap.connect(collector.analysis_export);
  end
  if (cfg.analysis_enable) begin
    monitor.out_monitor_ap.connect(analyzer.analysis_export);
  end
  if (cfg.use_reg_model) begin
    monitor.out_monitor_ap.connect(predictor.bus_in);
  end
endfunction

function void {{ module }}_master_agent::end_of_elaboration_phase(uvm_phase phase);
  if (cfg.use_reg_model) begin
    if (predictor.map == null)
      `uvm_fatal("end_of_elaboration_phase", "When register model used, the predictor map should be set")
  end
endfunction

`endif