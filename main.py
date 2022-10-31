import data
import machine

power = "off"

water = data.resources["water"]
milk = data.resources["milk"]
coffee = data.resources["coffee"]
money = 0

while power == "off":
    power = input("\nType 'on' to turn on: ")
    if power == "on":
        machine.coffeemach(water, milk, coffee, money)