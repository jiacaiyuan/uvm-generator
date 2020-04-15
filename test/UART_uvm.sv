class reg_uart_data extends uvm_reg;
   rand uvm_reg_field DATA;
   
   virtual function void build();
      DATA = uvm_reg_field::type_id::create("DATA", null, get_full_name());
      DATA.configure(this, 32, 0, "RW", 1, 'h0, 1, 1, 1);
   endfunction

   function new(string name = "reg_uart_data");
      super.new(name, 32, UVM_NO_COVERAGE);
   endfunction

   `uvm_object_utils(reg_uart_data)
endclass

class reg_uart_state extends uvm_reg;
   rand uvm_reg_field STATE;
   
   virtual function void build();
      STATE = uvm_reg_field::type_id::create("STATE", null, get_full_name());
      STATE.configure(this, 32, 0, "RW", 1, 'h0, 1, 1, 1);
   endfunction

   function new(string name = "reg_uart_state");
      super.new(name, 32, UVM_NO_COVERAGE);
   endfunction

   `uvm_object_utils(reg_uart_state)
endclass

class reg_uart_ctrl extends uvm_reg;
   rand uvm_reg_field CTRL;
   
   virtual function void build();
      CTRL = uvm_reg_field::type_id::create("CTRL", null, get_full_name());
      CTRL.configure(this, 32, 0, "RW", 1, 'h0, 1, 1, 1);
   endfunction

   function new(string name = "reg_uart_ctrl");
      super.new(name, 32, UVM_NO_COVERAGE);
   endfunction

   `uvm_object_utils(reg_uart_ctrl)
endclass

class reg_uart_intclear extends uvm_reg;
   rand uvm_reg_field INTCLEAR;
   
   virtual function void build();
      INTCLEAR = uvm_reg_field::type_id::create("INTCLEAR", null, get_full_name());
      INTCLEAR.configure(this, 32, 0, "RO", 1, 'h0, 1, 0, 1);
   endfunction

   function new(string name = "reg_uart_intclear");
      super.new(name, 32, UVM_NO_COVERAGE);
   endfunction

   `uvm_object_utils(reg_uart_intclear)
endclass

class reg_uart_intstatus extends uvm_reg;
   rand uvm_reg_field INTSTATUS;
   
   virtual function void build();
      INTSTATUS = uvm_reg_field::type_id::create("INTSTATUS", null, get_full_name());
      INTSTATUS.configure(this, 32, 0, "WO", 1, 'h0, 1, 1, 1);
   endfunction

   function new(string name = "reg_uart_intstatus");
      super.new(name, 32, UVM_NO_COVERAGE);
   endfunction

   `uvm_object_utils(reg_uart_intstatus)
endclass

class reg_uart_bauddiv extends uvm_reg;
   rand uvm_reg_field BAUDDIV;
   
   virtual function void build();
      BAUDDIV = uvm_reg_field::type_id::create("BAUDDIV", null, get_full_name());
      BAUDDIV.configure(this, 32, 0, "RW", 1, 'h0, 1, 1, 1);
   endfunction

   function new(string name = "reg_uart_bauddiv");
      super.new(name, 32, UVM_NO_COVERAGE);
   endfunction

   `uvm_object_utils(reg_uart_bauddiv)
endclass

class reg_uart_abc extends uvm_reg;
   rand uvm_reg_field ABC;
   
   virtual function void build();
      ABC = uvm_reg_field::type_id::create("ABC", null, get_full_name());
      ABC.configure(this, 32, 0, "RW", 1, 'h0, 1, 1, 1);
   endfunction

   function new(string name = "reg_uart_abc");
      super.new(name, 32, UVM_NO_COVERAGE);
   endfunction

   `uvm_object_utils(reg_uart_abc)
endclass

class reg_uart_bcd extends uvm_reg;
   rand uvm_reg_field BCD;
   
   virtual function void build();
      BCD = uvm_reg_field::type_id::create("BCD", null, get_full_name());
      BCD.configure(this, 16, 0, "RW", 1, 'h0, 1, 1, 1);
   endfunction

   function new(string name = "reg_uart_bcd");
      super.new(name, 32, UVM_NO_COVERAGE);
   endfunction

   `uvm_object_utils(reg_uart_bcd)
endclass

class reg_uart_cde extends uvm_reg;
   rand uvm_reg_field CDE;
   
   virtual function void build();
      CDE = uvm_reg_field::type_id::create("CDE", null, get_full_name());
      CDE.configure(this, 32, 0, "RW", 1, 'h0, 1, 1, 1);
   endfunction

   function new(string name = "reg_uart_cde");
      super.new(name, 32, UVM_NO_COVERAGE);
   endfunction

   `uvm_object_utils(reg_uart_cde)
endclass

class UART extends uvm_reg_block;
   rand reg_uart_data DATA;
   rand reg_uart_state STATE;
   rand reg_uart_ctrl CTRL;
   rand reg_uart_intclear INTCLEAR;
   rand reg_uart_intstatus INTSTATUS;
   rand reg_uart_bauddiv BAUDDIV;
   rand reg_uart_abc ABC;
   rand reg_uart_bcd BCD;
   rand reg_uart_cde CDE;

   `uvm_object_utils(UART)
   function new(string name = "UART");
      super.new(name, UVM_NO_COVERAGE);
   endfunction 
   
   virtual function void build();
      default_map = create_map("default_map", `UVM_REG_ADDR_WIDTH'h0, 4, UVM_LITTLE_ENDIAN, 1);
      DATA = reg_uart_data::type_id::create("DATA");
      DATA.configure(this, null, "DATA");
      DATA.build();
      default_map.add_reg(DATA, `UVM_REG_ADDR_WIDTH'h0, "RW", 0);
      STATE = reg_uart_state::type_id::create("STATE");
      STATE.configure(this, null, "STATE");
      STATE.build();
      default_map.add_reg(STATE, `UVM_REG_ADDR_WIDTH'h4, "RW", 0);
      CTRL = reg_uart_ctrl::type_id::create("CTRL");
      CTRL.configure(this, null, "CTRL");
      CTRL.build();
      default_map.add_reg(CTRL, `UVM_REG_ADDR_WIDTH'h8, "RW", 0);
      INTCLEAR = reg_uart_intclear::type_id::create("INTCLEAR");
      INTCLEAR.configure(this, null, "INTCLEAR");
      INTCLEAR.build();
      default_map.add_reg(INTCLEAR, `UVM_REG_ADDR_WIDTH'hc, "RO", 0);
      INTSTATUS = reg_uart_intstatus::type_id::create("INTSTATUS");
      INTSTATUS.configure(this, null, "INTSTATUS");
      INTSTATUS.build();
      default_map.add_reg(INTSTATUS, `UVM_REG_ADDR_WIDTH'hc, "WO", 0);
      BAUDDIV = reg_uart_bauddiv::type_id::create("BAUDDIV");
      BAUDDIV.configure(this, null, "BAUDDIV");
      BAUDDIV.build();
      default_map.add_reg(BAUDDIV, `UVM_REG_ADDR_WIDTH'h10, "RW", 0);
      ABC = reg_uart_abc::type_id::create("ABC");
      ABC.configure(this, null, "ABC");
      ABC.build();
      default_map.add_reg(ABC, `UVM_REG_ADDR_WIDTH'h1c, "RW", 0);
      BCD = reg_uart_bcd::type_id::create("BCD");
      BCD.configure(this, null, "BCD");
      BCD.build();
      default_map.add_reg(BCD, `UVM_REG_ADDR_WIDTH'h24, "RW", 0);
      CDE = reg_uart_cde::type_id::create("CDE");
      CDE.configure(this, null, "CDE");
      CDE.build();
      default_map.add_reg(CDE, `UVM_REG_ADDR_WIDTH'h28, "RW", 0);
   endfunction
endclass
