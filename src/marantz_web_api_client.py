"""
provides functions for some of the marantz AVR web api endpoints
"""

from enum import Enum
import requests
import yaml

class MarantzPowerState(Enum):
    ON = "ON"
    OFF = "STANDBY"

def turn_marantz_on():
    change_marantz_power_state(MarantzPowerState.ON)

def turn_marantz_off():
    change_marantz_power_state(MarantzPowerState.OFF)

def change_marantz_power_state(state: MarantzPowerState):
    # build the endpoint with info from config file
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    ip = config['marantz_ip']
    path = config['marantz_endpoint']
    ENDPOINT = f"http://{ip}/{path}"
    print(ENDPOINT)

    # build the data payload
    data = {
        "cmd0": f"PutSystem_OnStandby/{state.value}"
    }

    # send the request
    try:
        response = requests.post(ENDPOINT, data=data)

        if response.status_code == 200:
            print(f"Successfully sent {state} command.")
        else:
            print(f"Failed to send {state} command. Status code: {response.status_code}")
            print(response.text)

    except requests.RequestException as e:
        print(f"Error communicating with AVR: {e}")


if __name__ == '__main__':
    # turn_marantz_on()
    turn_marantz_off()