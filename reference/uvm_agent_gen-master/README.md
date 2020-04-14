# uvm_agent_gen
UVM Agent Generator

UVM Agents have a uniform structure something that can be templated.   One issue
with templates within typical IDEs is that they generate code for a single file,
not a set of related files.  This script generates the entire set of inter-related
files for a UVM Agent with a file structure recommended by the UVM library.


# Installation

I haven't packaged this yet, so you will have to clone it from the repo

    git clone https://github.com/blargony/uvm_agent_gen.git


# Operation

Run the agent_gen.py script at the command line.  It requires a few arguments:

     --agent_name [name_of_your_agent]
     --dest [generated_agent_directory]



