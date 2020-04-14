# yuu_vip_gen
UVM VIP architecture generator

## Useage
yuu_vip_gen.py [-h] -m MODULE [-p PREFIX] [-o OUTPUT] [-e]  
　　　　　　　[--addr_width ADDR_WIDTH] [--data_width DATA_WIDTH]

optional arguments:  
　-h, --help            show this help message and exit  
　-m MODULE, --module MODULE  
　　　　　　　　　　　[Required] Expected module name  
　-p PREFIX, --prefix PREFIX  
　　　　　　　　　　　[Optional] Module prefix  
　-o OUTPUT, --output OUTPUT  
　　　　　　　　　　　[Optional] Output path  
　-e, --env　　　　　　[Optional] Including master/slave/environment  
　--addr_width ADDR_WIDTH  
　　　　　　　　　　　[Optional] Transaction address width  
　--data_width DATA_WIDTH  
　　　　　　　　　　　[Optional] Transaction data width  
