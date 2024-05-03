## MANUAL TEC


# Topologia





|     VLAN     | Encabezado 2 | Encabezado 3 | Ecnabezado | Ecbaezado | boludooo | sfksjfls | fsfsfsfs | fsfssdfs |
|--------------|--------------|--------------|------------|-----------|----------|----------|----------|----------|         
| Venta     | Valor 2      | Valor 3      |            |           |          |          |          |          |
| informatica     | Valor 5      | Valor 6      |            |           |          |          |          |          |


#  Cracion interfaz virtual con HSRP
  
  R1(config)# interface [tipo] [número]
  R1(config-if)# standby [grupo] ip [Dirección IP virtual]
  R1(config-if)# standby [grupo] priority [prioridad]
  R1(config-if)# standby [grupo] preempt


#  Creación de PortChannel con LACP
  
  SW0(config)# interface range [tipo] [rango]
  SW0(config-if-range)# channel-group [grupo] mode active

  SW1(config)# interface range [tipo] [rango]
  SW1(config-if-range)# channel-group [grupo] mode active

# Creacion una dirección IP para la interfaz
  
  R1(config)# interface [tipo] [número]
  R1(config-if)# ip address [dirección IP] [máscara de subred]