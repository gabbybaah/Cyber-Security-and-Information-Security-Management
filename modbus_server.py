from pyModbusTCP.server import ModbusServer
import time
server = ModbusServer("127.0.0.1", 502, no_block=True)
server.start()
server.data_bank.set_holding_registers(0, [17, 17, 17, 17, 17])
while True:
    time.sleep(1)
