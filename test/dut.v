module dut #(parameter ADDR_WIDTH=32 ,parameter DATA_WIDTH=32)
(
//bus side
input wire PClk,
input wire PCLKG,
input wire PRESETn,
input wire PSEL,
input wire [ADDR_WIDTH<<2-1:2] pAddr,
input wire penable,
input wire PWRite,
input wire [DATA_WIDTH-1:0] PWDATA,
output wire [31:0] prdata,
output wire pready,
output wire pslverr,

//master side
input RXD,
input [31:0] data_st,
input [31:0] addr_st,
input [7:0] control,
output request,
output [2:0] valid,
output [31:0] data_ld,
output [31:0] addr_ld,

//slave side
output TXD,
output [7:0] data_wrt,
output [7:0] addr_wrt,
output regrant,
input [3:0] confirm,
input [7:0] data_rd,
input [7:0] addr_rd
);


endmodule
