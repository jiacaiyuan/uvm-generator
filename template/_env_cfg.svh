//***** ***** ***** *****  *****  *****  *****  *****  *****  *****  ***** 
//Auto Generated by UVM-Generator
//Author: Jiacai Yuan
//E-mail: yuan861025184@163.com
//Contents:{{MODULE}}_env_config {{MODULE}}_callback
//***** ***** ***** *****  *****  *****  *****  *****  *****  *****  ***** 
class {{MODULE}}_env_config extends uvm_object;
	// Add user cfg here
	
	// User cfg ends
	`uvm_object_utils_begin({{MODULE}}_env_config)
	// Add user cfg here
	//e.g. `uvm_field_int
	// User cfg ends
	`uvm_object_utils_end
	function new(string name="{{MODULE}}_config");
		super.new(name);
	endfunction
endclass

class {{MODULE}}_callback extends uvm_callback;
	`uvm_object_utils({{MODULE}}_callback)
	
	//Constructor Function
	function new(string name="{{MODULE}}_callback");
		super.new(name);
	endfunction
	{{method}}
	// Add user method here

	// User method ends	
endclass 