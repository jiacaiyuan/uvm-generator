`ifndef {{ module.upper() }}_SLAVE_AGENT_SV
`define {{ module.upper() }}_SLAVE_AGENT_SV

class {{ module }}_slave_agent extends uvm_agent;
  // Data members
  {{ module }}_slave_config cfg;

  {{ module }}_slave_sequencer sequencer;
  {{ module }}_slave_driver    driver;
  {{ module }}_slave_monitor   monitor;
  {{ module }}_slave_collector collector;
  {{ module }}_slave_analyzer  analyzer;

  uvm_analysis_port #({{ module }}_slave_item) out_driver_ap;
  uvm_analysis_port #({{ module }}_slave_item) out_monitor_ap;

  `uvm_component_utils_begin({{ module }}_slave_agent)
  `uvm_component_utils_end

  // Function declarations
  extern         function      new(string name, uvm_component parent);
  extern virtual function void build_phase(uvm_phase phase);
  extern virtual function void connect_phase(uvm_phase phase);
endclass

function {{ module }}_slave_agent::new(string name, uvm_component parent);
  super.new(name, parent);
endfunction

function void {{ module }}_slave_agent::build_phase(uvm_phase phase);
  if (!uvm_config_db #({{ module }}_slave_config)::get(null, get_full_name(), "cfg", cfg) && cfg == null)
    `uvm_fatal("build_phase", "Cannot get {{ module }} slave configuration");
  if (cfg == null)
    `uvm_fatal("build_phase", "Get a null {{ module }} slave configuration")

  monitor = {{ module }}_slave_monitor::type_id::create("monitor", this);
  monitor.cfg = cfg;
  if (cfg.is_active == UVM_ACTIVE) begin
    uvm_config_db #({{ module }}_slave_config)::set(this, "sequencer", "cfg", cfg);
    sequencer = {{ module }}_slave_sequencer::type_id::create("sequencer", this);
    driver = {{ module }}_slave_driver::type_id::create("driver", this);
    sequencer.cfg = cfg;
    driver.cfg = cfg;
  end
  if (cfg.coverage_enable) begin
    collector = {{ module }}_slave_collector::type_id::create("collector", this);
    collector.cfg = cfg;
  end
  if (cfg.analysis_enable) begin
    analyzer = {{ module }}_slave_analyzer::type_id::create("analyzer", this);
    analyzer.cfg = cfg;
  end
endfunction

function void {{ module }}_slave_agent::connect_phase(uvm_phase phase);
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
endfunction

`endif