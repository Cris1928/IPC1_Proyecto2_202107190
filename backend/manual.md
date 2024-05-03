#  MANUAL TEC 


## Topologia 



## JUTIAPA 

|     VLAN     | ID | EQUIPOS | MASCARA | WILDCARD | ID RED | PRIMERA IP | ULTIMA IP | IP BRODCAST |
|--------------|--------------|--------------|------------|-----------|----------|----------|----------|----------|         
| Venta | 31 | 25 | 255.255.255.224 | 0.0.0.31 | 192.168.10.0 | 192.168.10.1 | 192.168.10.30 | 192.168.10.31 |
| Informatica | 41 | 12 | 255.255.255.40 | 0.0.0.15 | 192.168.10.32 | 192.168.10.33 | 192.168.10.46 | 192.168.10.47 |
| RRHH | 21 | 4 | 255.255.255.240 | 0.0.0.15 | 192.168.10.48 | 192.168.10.49 | 192.168.10.62 | 192.168.10.63 |
| Contabilidad | 21 | 4 | 255.255.255.248 | 0.0.0.7 | 192.168.10.64 | 192.168.10.65 | 192.168.10.70 | 192.168.10.71 |

## ESCUINTLA 

|     VLAN     | ID | EQUIPOS | MASCARA | WILDCARD | ID RED | PRIMERA IP | ULTIMA IP | IP BRODCAST |
|--------------|--------------|--------------|------------|-----------|----------|----------|----------|----------|         
| Venta | 31 | 25 | 255.255.255.224 | 0.0.0.31 | 192.168.10.0 | 192.168.10.1 | 192.168.10.30 | 192.168.10.31 |
| RRHH | 11 | 5 | 255.255.255.248 | 0.0.0.7 | 192.168.10.32 | 192.168.10.33 | 192.168.10.38 | 192.168.10.39 |

## QUICHE 

|     VLAN     | ID | EQUIPOS | MASCARA | WILDCARD | ID RED | PRIMERA IP | ULTIMA IP | IP BRODCAST |
|--------------|--------------|--------------|------------|-----------|----------|----------|----------|----------|         
| Venta | 31 | 36 | 255.255.255.192 | 0.0.0.63 | 192.168.10.0 | 192.168.10.1 | 192.168.10.62 | 192.168.10.63 |
| TI | 41 | 21 | 255.255.255.244 | 0.0.0.31 | 192.168.10.64 | 192.168.10.65 | 192.168.10.94 | 192.168.10.95 |
| RRHH | 11 | 12 | 255.255.255.240 | 0.0.0.15 | 192.168.10.96 | 192.168.10.97 | 192.168.10.110 | 192.168.10.111 |
| Contabilidad | 21 | 10 | 255.255.255.240 | 0.0.0.15 | 192.168.10.112 | 192.168.10.113 | 192.168.10.126 | 192.168.10.127 |


## PETEN 

|     VLAN     | ID | EQUIPOS | MASCARA | WILDCARD | ID RED | PRIMERA IP | ULTIMA IP | IP BRODCAST |
|--------------|--------------|--------------|------------|-----------|----------|----------|----------|----------|         
| Venta | 31 | 30 | 255.255.255.224 | 0.0.0.31 | 192.168.10.0 | 192.168.10.1 | 192.168.10.30 | 192.168.10.31 |
| TI | 41 | 15 | 255.255.255.224 | 0.0.0.31 | 192.168.10.32 | 192.168.10.33 | 192.168.10.62 | 192.168.10.63 |
| RRHH | 11 | 10 | 255.255.255.240 | 0.0.0.15 | 192.168.10.64 | 192.168.10.65 | 192.168.10.78 | 192.168.10.79 |



##  Cracion interfaz virtual con HSRP
  
  R1(config)# interface [tipo] [número]
  R1(config-if)# standby [grupo] ip [Dirección IP virtual]
  R1(config-if)# standby [grupo] priority [prioridad]
  R1(config-if)# standby [grupo] preempt


##  Creación de PortChannel con LACP
  
  SW0(config)# interface range [tipo] [rango]
  SW0(config-if-range)# channel-group [grupo] mode active

  SW1(config)# interface range [tipo] [rango]
  SW1(config-if-range)# channel-group [grupo] mode active

## Creacion una dirección IP para la interfaz
  
  R1(config)# interface [tipo] [número] 
  R1(config-if)# ip address [dirección IP] [máscara de subred] 


  - Swtich VTP modo servidor
  Configuración VTP en modo servidor en el switch servidor.
   
    ```
    SW1(config)# vtp version 2
    SW1(config)# vtp mode server


- Interfaz modo truncal
  Configuramos las interfaces que se conectan con otros switichs en modo truncal, pasamos las Vlan que nos interesan
   
    
    SW1(config)# interface fa0/1
    SW1(config-if)# switchport trunk encapsulation dot1q
    SW1(config-if)# switchport mode trunk
    SW1(config-if)#switchport trunk allowed vlan 1, 11,21 ,31, 41 ,1002-1005


- Switch VTP modo cliente
  Configuramos el switch en modo cliente en el mismo dominio en el que estan nuestras Vlan's

    ```
    SW2(config)# vtp version 2
    SW2(config)# vtp mode client


- Interfaz modo access
  Configuramos nuestra interfaz con dispositivos finales y le asignamos una Vlan especifica

    
    SW2(config)# interface FastEthernet 0/1
    SW2(config-if)# switchport mode access
    SW2(config-if)# switchport access vlan <número-de-VLAN>




- Declarar Vlan's
  Creamos y definimos las Vlan's que usaremos en nuestra red
   
    
    SW1(config)# vlan No.Vlan
    SW1(config-vlan)# name nombreVlan
    SW1(config-vlan)# exit

-  Crear las subinterfaces

Router(config)# interface tipo número
Router(config-if)# encapsulation dot1Q número_de_VLAN
Router(config-if)# ip address dirección_IP máscara_de_subred