//***** ***** ***** *****  *****  *****  *****  *****  *****  *****  ***** 
//Auto Generated by UVM-Generator
//Author: Jiacai Yuan
//E-mail: yuan861025184@163.com
//Contents:{{MODULE}}_{{MASTER_SLAVE_BUS}}_tranaction(request & response)
//***** ***** ***** *****  *****  *****  *****  *****  *****  *****  ***** 
{%for i in range(0,2)%}
{%if i==0%} {%set name="req"%}
{%elif i==1 and response%}{%set name="rsp"%}
{%else%}{%set name=""%}
{%endif%}
{%if name%}
class {{MASTER_SLAVE_BUS}}_{{name}} extends uvm_sequence_item;
	// Add user data here
	//e.g. rand int addr
	// User data ends
	`uvm_object_utils_begin({{MASTER_SLAVE_BUS}}_{{name}})
	// Add user data here
	//e.g. `uvm_field_int
	// User data ends
	`uvm_object_utils_end
	function new(string name="{{MASTER_SLAVE_BUS}}_{{name}}");
		super.new(name);
	endfunction
	{{method}}
	// Add user method here
	//e.g. implement constarins
	// User method ends	
endclass
{%endif%}
{%endfor%}