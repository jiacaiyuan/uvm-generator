clean:
	-rm -rf bus*.sv slave*.sv master*.sv dut*.sv
	-rm -rf simv* csrc *.h
cmp:
	vcs -full64 +v2k -sverilog -f fil.lst -ntb_opts uvm-1.2 -debug_all -timescale=1ns/1ps

run:
	./simv +UVM_TESTNAME=dut_base_test