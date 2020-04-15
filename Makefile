.PHONY:clean
clean:
	-rm -rf build
	make clean -C ./auto_instance
	make clean -C ./systemrdl
	make clean -C ./ralbot
	make clean -C ./generator
	make clean -C ./test

.PHONY:demo
demo:
	python3 top.py -i ./demo/dut.json  -o ./build

