`ifndef {{ module.upper() }}_TYPE_SV
`define {{ module.upper() }}_TYPE_SV

  typedef enum bit {
    False,
    True
  } boolean;
  
  typedef bit [`{{ module.upper() }}_ADDR_WIDTH-1:0] {{ module }}_addr_t;
  typedef bit [`{{ module.upper() }}_DATA_WIDTH-1:0] {{ module }}_data_t;

  typedef class {{ module }}_item;
  typedef uvm_reg_predictor #({{ module }}_item) {{ module }}_predictor;

`endif
