//***** ***** ***** *****  *****  *****  *****  *****  *****  *****  ***** 
//Auto Generated by UVM-Generator
//Author: Jiacai Yuan
//E-mail: yuan861025184@163.com
//Contents:dut_master_tranaction(request & response)
//***** ***** ***** *****  *****  *****  *****  *****  *****  *****  ***** 

 


class master_req extends uvm_sequence_item;
	// Add user data here
	//e.g. rand int addr
	// User data ends
	`uvm_object_utils_begin(master_req)
	// Add user data here
	//e.g. `uvm_field_int
	// User data ends
	`uvm_object_utils_end
	function new(string name="master_req");
		super.new(name);
	endfunction
	
	// Add user method here
	//e.g. implement constarins
	// User method ends	
endclass





class master_rsp extends uvm_sequence_item;
	// Add user data here
	//e.g. rand int addr
	// User data ends
	`uvm_object_utils_begin(master_rsp)
	// Add user data here
	//e.g. `uvm_field_int
	// User data ends
	`uvm_object_utils_end
	function new(string name="master_rsp");
		super.new(name);
	endfunction
	
	// Add user method here
	//e.g. implement constarins
	// User method ends	
endclass
