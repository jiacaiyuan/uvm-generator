#!/usr/bin/env sh
irun -uvm +incdir+../src +incdir+../sequence_lib/src ../src/{{ agent.name }}_if.sv ../src/{{ agent.name }}_pkg.sv

