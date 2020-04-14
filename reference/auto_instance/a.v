
function abc();

/*abc
*/

endfunction

module 


a
(input wire [3:0]x,
output  logic [2:0]y,
output wire z);
parameter WID=2;
//input [3:0] x;
//output logic [2:0] y;
//output wire z;
//abc
function abc();

/*abc
*/
parameter A=16,B=2;
endfunction
initial
begin
	$display("hello a");
end
//dec
endmodule

module b(q,w,e);
input [3:0] q;
output logic [2:0] w;
output wire e;
/*abc
*/

initial
begin
	$display("hello b");
end
endmodule
