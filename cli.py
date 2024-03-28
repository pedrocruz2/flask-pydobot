import typer
import inquirer
from yaspin import yaspin
import time
import pydobot
from serial.tools import list_ports


app = typer.Typer()

# Estado da ferramenta
robot_tool = False

available_ports = list_ports.comports()

porta_escolhida = inquirer.prompt([inquirer.List("porta", message="Escolha a porta serial", choices=[x.device for x in available_ports])])["porta"]

print('Porta escolhida:', porta_escolhida)

robo = pydobot.Dobot(port=porta_escolhida, verbose=False)
print(robo.pose())