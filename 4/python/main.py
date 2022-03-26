from Vehicle import Vehicle
from Ship import Ship
from Airplane import Airplane
from Person import Person
from Job import Job
from Driver import Driver

airplane1 = Airplane("Garuda", "Solar", 100, 3, "Large", 10)
airplane1.show()

airplane2 = Airplane()
airplane2.setName("Batik Air")
airplane2.setFuelType("Pertalite")
airplane2.setMaxPassengers(75)
airplane2.setAge(2)
airplane2.setType("medium")
airplane2.setWingsLength(10)
airplane2.show()

ship1 = Ship("Emirated", "Pertamax", 40, 1, "Large", "Arab")
ship1.show()

ship2 = Ship()
ship2.setName("Titanic")
ship2.setFuelType("Premium")
ship2.setMaxPassengers(50)
ship2.setAge(5)
ship2.setType("Very Large")
ship2.setCountryOfManufacture("America")
ship2.show()

person1 = Person("2003941", "Novaldi Sandi Ago", "Male", "19216801", "Google", "CTO", 27, "27-10-2022", "BMW")
person1.show()

# create array of ship class, with 5 dummy data
# ship = [Ship("South Korea", 399.2, 58.6, "Atlantic Ocean"), Ship("China", 350.0, 43, "Hindia Ocean"), Ship("United States", 100.59, 16.24, "Atlantic Ocean"), Ship("United States", 85.3, 12.2, "Hindia Ocean"), Ship("United States", 82.2, 12.95, "Pacific Ocean")]

# # set ships derived attribute from Vehicle class
# ship[0].setModelName("Maersk Triple E class")
# ship[0].setAge(5)
# ship[0].setFuelType("Solar")
# ship[0].setMaxPassengers(10000)
# ship[0].setType("Container Ship")
# ship[1].setModelName("COSCO Guangzhou")
# ship[1].setAge(7)
# ship[1].setFuelType("Biofuels")
# ship[1].setMaxPassengers(9000)
# ship[1].setType("Neo Panamax")
# ship[2].setModelName("MV TransAtlantic")
# ship[2].setAge(3)
# ship[2].setFuelType("Distillites Fuel")
# ship[2].setMaxPassengers(4000)
# ship[2].setType("FeederMax")
# ship[3].setModelName("USS Enceladus (AK-80)")
# ship[3].setAge(1)
# ship[3].setFuelType("Biofuels")
# ship[3].setMaxPassengers(1000)
# ship[3].setType("Coastal Tanker")
# ship[4].setModelName("Falls of Clyde")
# ship[4].setAge(10)
# ship[4].setFuelType("Distillites Fuel")
# ship[4].setMaxPassengers(5000)
# ship[4].setType("VLCC")

# # show all the attribute, including derived attribute, of ship class
# print("                 SHIP CLASS")
# print("=================================================")
# for i in range(0,5):
#     ship[i].ShowClass()
# print("=================================================")

# # create array of airplane class, with 5 dummy data
# airplane = [Airplane(43.90, "Fixed Wing", "Wide", "General Electric CF6, Pratt & Whitney PW4000"), Airplane(11.50, "Fixed Wing", "Narrow", "Continental O-470"), Airplane(13.00, "Fixed Wing", "Narrow", "C: 2 x 65.3 kN P&W F100-PW-200 (2 x 107.7 kN with afterburner) turbofans."), Airplane(11.90, "Fixed Wing", "Narrow", "Garrett AiResearch TPE-331"), Airplane(51.70, "Fixed Wing", "Wide", "General Electric CF6, Pratt & Whitney PW4000")] 
# # set airplane derived attribute from Vehicle class

# airplane[0].setModelName("AIRBUS A-310")
# airplane[0].setAge(3)
# airplane[0].setMaxPassengers(300)
# airplane[0].setType("AIRBUS")
# airplane[0].setFuelType("Aviation Fuel")

# airplane[1].setModelName("BEECH 55 Baron")
# airplane[1].setAge(5)
# airplane[1].setMaxPassengers(3)
# airplane[1].setType("55 Baron")
# airplane[1].setFuelType("100LL")

# airplane[2].setModelName("BOEING F-15 Strike Eagle")
# airplane[2].setAge(2)
# airplane[2].setMaxPassengers(2)
# airplane[2].setType("BOEING")
# airplane[2].setFuelType("Kerosene-gasoline mixture")

# airplane[3].setModelName("MITSUBISHI LR-1")
# airplane[3].setAge(10)
# airplane[3].setMaxPassengers(6)
# airplane[3].setType("MITSUBISHI")
# airplane[3].setFuelType("Aviation Fuel")

# airplane[4].setModelName("MCDONNELL DOUGLAS MD-11")
# airplane[4].setAge(5)
# airplane[4].setMaxPassengers(400)
# airplane[4].setType("MCDONNELL DOUGLAS")
# airplane[4].setFuelType("Aviation Fuel")

# # show all the attribute, including derived attribute, of airplane class
# print("               AIRPLANE CLASS")

# print("=================================================")
# for i in range(0,5):
#     airplane[i].ShowClass()
# print("=================================================")

# # create arrau of class person, with 5 dummy data
# person = [Person("3501980908020004", "Roronoa Zoro", "Laki-Laki", Driver("AL001", "24 Maret 2024", "Car")), Person("3501180346720007", "Vinsmoke Sanji", "Laki-Laki", Driver("AL002", "12 Juni 2025", "Motorcycle")), Person("35124980902320012", "Nami", "Perempuan", Driver("AL006", "02 Juni 2030", "Car")), Person("350432809012020215", "God Usop", "Laki-Laki", Driver("AL056", "07 Maret 2024", "Plane")), Person("3651380948621024", "Nico Robin", "Perempuan", Driver("AL005", "24 Maret 2026", "Car"))]

# # set driver derived attribute from Job class
# person[0].getDriver().setNip("23098767")
# person[0].getDriver().setCompanyName("Grab")
# person[0].getDriver().setPosition("Employee")

# person[1].getDriver().setNip("32894375")
# person[1].getDriver().setCompanyName("Grab")
# person[1].getDriver().setPosition("Employee")

# person[2].getDriver().setNip("12874923")
# person[2].getDriver().setCompanyName("Go Car")
# person[2].getDriver().setPosition("Employee")

# person[3].getDriver().setNip("09827849")
# person[3].getDriver().setCompanyName("Go Car")
# person[3].getDriver().setPosition("Employee")

# person[4].getDriver().setNip("98876738")
# person[4].getDriver().setCompanyName("Blue Bird")
# person[4].getDriver().setPosition("Employee")

# # show all the attribute, including derived attribute, of person class
# print("               PERSON CLASS")

# print("=================================================")
# for i in range(0,5):
#     person[i].ShowClass()
# print("=================================================")