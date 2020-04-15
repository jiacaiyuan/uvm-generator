agent_test:
	python3 agent_test.py
config_test:
	python3 config_test.py
integrate_test:
	python3 integrate_test.py
clean:
	-rm -rf build
	-rm -rf bus*.sv slave*.sv master*.sv dut*.sv
	-rm -rf simv* csrc *.h
cmp:
	vcs -full64 +v2k -sverilog -f fil.lst -ntb_opts uvm-1.2 -debug_all -timescale=1ns/1ps

run:
	./simv +UVM_TESTNAME=dut_base_test
