# prepared import of enumerations
from model import Manufacturer, Transmission, Vehicle
# prepared csv module import
import csv
from typing import List

class VehicleFileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def import_vehicles_from_file(self):
        with open(self.file_path, 'r') as file:
            csv_reader = csv.reader(file)
            return self._transform_csv_vehicle_data_to_vehicles(csv_reader) 
        
    def _transform_csv_vehicle_data_to_vehicles(self, csv_reader):
        vehicles = []
        for row in csv_reader:
            vehicle_id = row[0]
            manufacturer = row[1]
            model = row[2]
            engine_power = int(row[3])
            price = float(row[4])
            color = row[5]
            mileage = int(row[6])
            year = int(row[7])
            fuel_type = row[8]
            transmission = row[9] 

            vehicle = Vehicle(vehicle_id,manufacturer,model,engine_power,price,color,mileage,year,fuel_type,transmission)
            vehicles.append(vehicle) 

        return vehicles      

    def rewrite_file(self, vehicle_list):
        with open(self.file_path, "w", newline = "" ) as file:
            csv_writer = csv.writer(file)
            for vehicle in vehicle_list:
                vehicle_string_for_rewrite = self.prepare_the_vehicle_for_rewriting("", vehicle)
                csv_writer.writerow(vehicle_string_for_rewrite.split(","))

    def prepare_the_vehicle_for_rewriting(self, vehicle_string_for_rewrite, vehicle):
        vehicle_attributes = [
            str(vehicle.get_vehicle_id()),
            vehicle.get_manufacturer(),
            vehicle.get_model(),
            str(vehicle.get_engine_power()),
            str(vehicle.get_price()),
            vehicle.get_color(),
            str(vehicle.get_mileage()),
            str(vehicle.get_year()),
            vehicle.get_fuel_type(),
            vehicle.get_transmission() 
        ]

        vehicle_string_for_rewrite = ','.join(vehicle_attributes)
        return vehicle_string_for_rewrite


class VehicleShopPrinter:

    def create_vehicle_list():
        return[
            Vehicle(1, "SKODA", "Superb", 190, 31000, "BLACK", 5000, 2015, "GASOLINE", "AUTOMATIC"),
            Vehicle(2, "AUDI", "A8", 460, 92000, "WHITE", 7500, 2019, "DIESEL_FUEL", "AUTOMATIC"),
            Vehicle(3, "VW", "Golf7", 220, 39000, "BLUE", 15000, 2012, "GASOLINE", "MANUAL"),
            Vehicle(4, "BMW", "X6", 320, 59000, "BLACK", 15000, 2012, "DIESEL_FUEL", "AUTOMATIC"),
            Vehicle(5, "BMW", "X5", 300, 39000, "WHITE", 153000, 2010, "DIESEL_FUEL", "AUTOMATIC"),
            Vehicle(6, "VW", "Tiguan", 420, 39000, "GREY", 15000, 2012, "DIESEL_FUEL", "AUTOMATIC"),
            Vehicle(7, "VW", "Passat", 220, 25000, "BROWN", 165000, 2013, "GASOLINE", "MANUAL"),
            Vehicle(8, "BMW", "530d", 187, 59000, "BLACK", 23000, 2016, "DIESEL_FUEL", "AUTOMATIC"),
            Vehicle(9, "AUDI", "A3", 350, 29000, "RED", 34000, 2012, "DIESEL_FUEL", "MANUAL"),
            Vehicle(10, "HONDA", "Civic", 150, 7000, "GREY", 153000, 2011, "DIESEL_FUEL" ,"AUTOMATIC")
        ]
    
    def print_available_vehicles(self, vehicle_list):
        
        print("######################### CATALOG #######################")
    
        print("\nAvailable vehicles:")
        for vehicle in vehicle_list:
            print(f"ID: {vehicle.get_vehicle_id()}, \n"
                  f"Manufacturer: {vehicle.get_manufacturer()}, \n"
                  f"Model: {vehicle.get_model()}, \n"
                  f"Price: {vehicle.get_price()}, \n"
                  f"Engone Power: {vehicle.get_engine_power()}, \n"
                  f"Color: {vehicle.get_color()}, \n"
                  f"Mileage: {vehicle.get_mileage()}, \n"
                  f"Year: {vehicle.get_year()}, \n"
                  f"Fuel Type: {vehicle.get_fuel_type()}, \n"
                  f"Transmission: {vehicle.get_transmission()}, \n")

        print("######################### CATALOG #######################")

    def print_vehicle_sold_message(self, vehicle_chosen_id):
        print("\nVehicle with ID", vehicle_chosen_id, "was sold.")
    
    def print_vehicle_id_to_sell_message(self):
        print("\n\n Please enter the number (ID) of the vehicle you want to sell: ")



class VehicleShopProcessor:
    # responsible to sell a specified vehicle by id
    def sell_vehicle(self, vehicles_list, selected_vehicle_id):
        original_length = len(vehicles_list)

        print("Vehicle IDs after removal:", [vehicle.get_vehicle_id() for vehicle in vehicles_list])

        vehicles_list[:] = [vehicle for vehicle in vehicles_list if str(vehicle.get_vehicle_id()) != str(selected_vehicle_id)]

        if len(vehicles_list) < original_length:
            print("Vehicle with ID " + str(selected_vehicle_id) + " has been sold.")
        else:
            print("Vehicle with this ID " + str(selected_vehicle_id) + " not found in the list." )    
class VehicleTransformer:

    # transforms a data array into a {@link Vehicle} list 
	# @param vehicle data array
	# @return list of {@link Vehicle} objects

    def transform_data_as_string_array_to_vehicle_objects(self, vehicles_as_array: List[Vehicle]) -> List[Vehicle]:
        if isinstance(vehicles_as_array[0], Vehicle):
           return vehicles_as_array 
        vehicle_objects = []
        for vehicle_string in vehicles_as_array:
            vehicle_object = self.transform_to_vehicle_object(vehicle_string)
            vehicle_objects.append(vehicle_object)
        return vehicle_objects

    
    def transform_to_vehicle_object(self, vehicle_as_string: str) -> Vehicle:
        vehicle_as_array = vehicle_as_string.split(",")
        vehicle_id = int(vehicle_as_array[0])
        manufacturer = self.get_manufacturer_from_string(vehicle_as_array[1].strip())
        model = vehicle_as_array[2].strip()
        engine_power = int(vehicle_as_array[3])
        price = float(vehicle_as_array[4])
        color = vehicle_as_array[5].strip()
        mileage = int(vehicle_as_array[6])
        year = int(vehicle_as_array[7])
        fuel_type = vehicle_as_array[8].strip()
        transmission = vehicle_as_array[9].strip()

        return Vehicle(vehicle_id, manufacturer, model, engine_power, price, color, mileage, year, fuel_type, transmission)

    # Example for Enumeration processing to use for all other Enumerations
    def get_manufacturer_from_string(self, manufacturer_as_string):
        for manufacturer in Manufacturer:
            if manufacturer.name == manufacturer_as_string:
                return manufacturer
        raise ValueError("Manufacturer not supported: " + manufacturer_as_string)


