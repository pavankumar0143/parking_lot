from .parking_lot import ParkingLot

class RunCommands:
    """
    This class provides abstraction over ParkingLot so, that we can execute commads which are user friendly .

    ...

    Attributes
    ----------
    _parking_obj : ParkingLot

    Methods
    -------
    run_command(command_input):
        Executes the given the command
    """

    def __init__(self):
        self._parking_obj = ParkingLot()

    def run_command(self, command_input):
        """
        Checks the commands and calls the specific function of ParkingLot and returns the function result

        Parameters
        ----------
        command_input : list
            command_input[0] -> command
                allowed values
                    create_parking_lot
                    park
                    leave
                    status
                    registration_numbers_for_cars_with_colour
                    slot_numbers_for_cars_with_colour
                    slot_number_for_registration_number

        Returns
        -------
        return ParkingLot function output without any transformation
        """

        command = command_input[0]
        
        if command == "create_parking_lot":
            max_parking_slot = int(command_input[1].strip()) #TODO add expection handing to validate type of input
            return self._parking_obj.set_max_parking_slots(max_parking_slot)
            
        elif command == "park":
            car_details_obj = {
                "registration_no":command_input[1],
                "colour":command_input[2]
            }
            return self._parking_obj.allocate_slot(car_details_obj)

        elif command == "leave":
            slot = int(command_input[1])
            return self._parking_obj.deallocate_slot(slot)

        elif command == "status":
            return self._parking_obj.status()

        elif command == "registration_numbers_for_cars_with_colour":

            return_key = "registration_no" 
            query_key = "colour" 
            condition_value = command_input[1]

            return self._parking_obj.query(return_key, query_key, condition_value)
        
        elif command == "slot_numbers_for_cars_with_colour":

            return_key = "slot_number" 
            query_key = "colour" 
            condition_value = command_input[1]

            return self._parking_obj.query(return_key, query_key, condition_value)

        elif command == "slot_number_for_registration_number":

            return_key = "slot_number" 
            query_key = "registration_no" 
            condition_value = command_input[1]

            return self._parking_obj.query(return_key, query_key, condition_value)

        else:
            return "Invalid command"