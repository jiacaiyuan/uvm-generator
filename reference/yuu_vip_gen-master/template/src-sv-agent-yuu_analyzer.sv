`ifndef {{ module.upper() }}_ANALYZER_SV
`define {{ module.upper() }}_ANALYZER_SV

class {{ module }}_analyzer extends uvm_subscriber #({{ module }}_item);
  // Data members
  virtual {{ module }}_interface vif;

  {{ module }}_config cfg;
  uvm_event_pool events;

  protected time m_start_time;
  protected time m_end_time;
  protected bit  m_start = 0;
  protected int  m_count = 0;

  `uvm_component_utils_begin({{ module }}_analyzer)
  `uvm_component_utils_end

  // Function declarations
  extern                   function      new(string name, uvm_component parent);
  extern           virtual function void connect_phase(uvm_phase phase);
  extern           virtual task          run_phase(uvm_phase phase);
  extern           virtual function void report_phase(uvm_phase phase);

  extern           virtual function void write({{ module }}_item t);
  extern protected virtual task          measure_start();
  extern protected virtual task          measure_end();
endclass

function {{ module }}_analyzer::new(string name, uvm_component parent);
  super.new(name, parent);
endfunction

function void {{ module }}_analyzer::connect_phase(uvm_phase phase);
  this.vif = cfg.vif;
  this.events = cfg.events;
endfunction

task {{ module }}_analyzer::run_phase(uvm_phase phase);
  measure_start();
  measure_end();
endtask


function void {{ module }}_analyzer::report_phase(uvm_phase phase);
  real tput_rate;

  if (m_count == 0) begin
    `uvm_warning("report_phase", "Analyzer haven't received any transaction")
    return;
  end

  tput_rate = real'(m_count)/(m_end_time - m_start_time) * 1000;
  `uvm_info("report_phase", $sformatf("{{ module.upper() }} speed is %f", tput_rate), UVM_LOW);
endfunction

function void {{ module }}_analyzer::write({{ module }}_item t);
endfunction

task {{ module }}_analyzer::measure_start();
  uvm_event e = events.get($sformatf("%s_measure_begin", cfg.get_name()));

  e.wait_on();
  m_start_time = $realtime();
  m_start = 1;
  `uvm_info("measure_start", $sformatf("%s analyzer start measure @ %t", cfg.get_name(), m_start_time), UVM_LOW)
endtask

task {{ module }}_analyzer::measure_end();
  uvm_event e = events.get($sformatf("%s_measure_end", cfg.get_name()));

  e.wait_on();
  m_end_time = $realtime();
  m_start = 0;
  `uvm_info("measure_end", $sformatf("%s analyzer end measure @ %t", cfg.get_name(), m_end_time), UVM_LOW)
endtask

`endif