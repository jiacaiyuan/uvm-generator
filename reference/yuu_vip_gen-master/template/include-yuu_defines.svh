`ifndef {{ module.upper() }}_DEFINES_SVH
`define {{ module.upper() }}_DEFINES_SVH
  {% if use_env %}
  `ifndef {{ module.upper() }}_MASTER_NUM
  `define {{ module.upper() }}_MASTER_NUM  1
  `endif

  `ifndef {{ module.upper() }}_SLAVE_NUM
  `define {{ module.upper() }}_SLAVE_NUM  1
  `endif
  {% endif %}
  `ifndef {{ module.upper() }}_ADDR_WIDTH
  `define {{ module.upper() }}_ADDR_WIDTH  {{ addr_width }}
  `endif
  
  `ifndef {{ module.upper() }}_DATA_WIDTH
  `define {{ module.upper() }}_DATA_WIDTH  {{ data_width }}
  `endif
  {% if use_env %}
  `ifndef {{ module.upper() }}_MASTER_SETUP_TIME
  `define {{ module.upper() }}_MASTER_SETUP_TIME  1
  `endif

  `ifndef {{ module.upper() }}_MASTER_HOLD_TIME
  `define {{ module.upper() }}_MASTER_HOLD_TIME  1
  `endif

  `ifndef {{ module.upper() }}_SLAVE_SETUP_TIME
  `define {{ module.upper() }}_SLAVE_SETUP_TIME  1
  `endif

  `ifndef {{ module.upper() }}_SLAVE_HOLD_TIME
  `define {{ module.upper() }}_SLAVE_HOLD_TIME  1
  `endif
  {% else %}
  `ifndef {{ module.upper() }}_SETUP_TIME
  `define {{ module.upper() }}_SETUP_TIME  1
  `endif

  `ifndef {{ module.upper() }}_HOLD_TIME
  `define {{ module.upper() }}_HOLD_TIME  1
  `endif
  {% endif %} 
`endif