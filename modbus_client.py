from pyModbusTCP.client import ModbusClient
c = ModbusClient(host="127.0.0.1", port=502, auto_open=True)
registers = c.read_holding_registers(0, 5)
print("PLC holding registers 0-4:", registers)
