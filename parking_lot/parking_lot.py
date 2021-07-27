
class ParkingLot:
    """
    A class to represent a parking lot give access to manipulate its data.

    ...

    Attributes
    ----------
    _free_slots : int
        free slots available in parking lot
    _max_slots : int
        max slots available in parking lot
    _parking_data : list
        holds car info '{registration_no:"","colour":""}' in a list
    _EMPTY_SLOT : bool
        it is contast value -> 'False', which is used to represent empty slot in the _parking_data

    Methods
    -------
    set_max_parking_slots(no_of_slots):
        Intializes the 'Attributes' with given no_of_slots
    get_metadata():
        Returns present values in 'Attributes'
    get_free_slots_count():
        Returns _free_slots
    allocate_slot(car_details):
        Allocates nearest parking slot and returns slot number
    deallocate_slot(slot):
        Remove car from the given slot number
    query(return_key, query_key, condition_value):
        Returns query results based return_key, query_key and conditonal_value
    status():
        returns tab-delimited string of values present _parking_data

    """

    def __init__(self):
        
        self._free_slots = 0
        self._max_slots = 0
        self._parking_data = []
        self._EMPTY_SLOT = False

    def set_max_parking_slots(self, no_of_slots):
        """
        Intializes the 'Attributes' with given no_of_slots

        Parameters
        ----------
        no_of_slots : int

        Returns
        -------
        Created a parking lot with {no_of_slots} slots
        """
        
        self._free_slots = no_of_slots 
        self._max_slots = no_of_slots
        self._parking_data = [ self._EMPTY_SLOT for _ in range(self._free_slots)] # intailize the list with empty slots for a given range
        
        return "Created a parking lot with {max_slots} slots".format(max_slots=self._free_slots )

    def get_metadata(self):
        """
        Returns present values in 'Attributes'

        Returns
        -------
        Max Slots: {_max_slots} | Free Slots {_free_slots} | Length: {length(_parking_data)}
        """

        return "Max Slots: {slots} | Free Slots {free_slots} | Length: {length}".format(
            slots=self._max_slots,
            free_slots=self._free_slots,
            length=len(self._parking_data)
        )

    def get_free_slots_count(self):
        """
        Returns _free_slots

        Returns
        -------
        Free slots: {_free_slots}
        """
        return "Free slots: {count}".format(count=self._free_slots)

    
    def allocate_slot(self, car_details):
        """
        Allocates nearest parking slot and returns slot number
            if free_slots are available
                Gets nereast free slot , Assigns car_details to that slot, Decreases the avialble free slots, Returns allocated slot number
            else
                Returns free slots not available

        Parameters
        ----------
        car_details : dict
            dict of {"registration_no": "","colour":""}.

        Returns
        -------
        Allocated slot number: {slot_number} || Sorry, parking lot is full
        """
        
        if self._free_slots > 0:
            free_slot = self._parking_data.index(self._EMPTY_SLOT) # index returns first index occurance of the value
            self._parking_data[free_slot] = car_details
            self._free_slots = self._free_slots - 1
            return "Allocated slot number: {slot}".format(slot=free_slot + 1) # added plus one because list index starts at zero
        
        else:
            return "Sorry, parking lot is full"

    def deallocate_slot(self, slot):
        """
        Remove car details from the given slot number
            if slot numeber is greater than zero and slot is less than _max_slots
                Delete the car details from that slot and Increases _free_slot by one
            else
                Returns invalid slot number

        Parameters
        ----------
        slot : int

        Returns
        -------
        Allocated slot number: {slot_number} || Sorry, parking lot is full
        """

        if slot > 0 and slot <= self._max_slots:
            self._parking_data[slot-1] = False # reduce by one because list index starts at zero, for user starts at 1
            self._free_slots = self._free_slots + 1
            return "Slot number {slot} is free".format(slot=slot)
        else:
            return "Slot number {slot} is invalid".format(slot=slot)

    def query(self, return_key, query_key, condition_value):
        """
        Returns query results based return_key, query_key and conditonal_value

        Parameters
        ----------
        return_key : str
            allowed values 'registration_no,slot_number'
        query_key : str
            allowed values 'registration_no,colour'
        condition_value : str

        Returns
        -------
        coma sperated string of car_details[return_key] || Not found
        """
        
        result_list = []

        for idx, car_data in enumerate(self._parking_data):

            # print("query_key",query_key, "query_value",car_data[query_key], "condition_value",condition_value)
            
            if type(car_data) is not bool and car_data[query_key] == condition_value:

                if return_key == "slot_number":
                    result_list.append(str(idx+1))
                else:
                    result_list.append(car_data[return_key])
        
        if len(result_list) > 0:
            return ", ".join(result_list)
        else:
            return "Not found"


    def status(self):
        """
        Returns tab-delimited string of values present _parking_data

        Returns
        -------
        Slot No.\tRegistration No\tColour\n{sr_no}\t{registration_no}\t{colour}
        """
        
        header = "Slot No.\tRegistration No\tColour"
        fmt_str = "{sr_no}\t{registration_no}\t{colour}"
        result_set = [header]
        
        for idx, data in enumerate(self._parking_data):
            
            if type(data) is not bool:
                result_set.append(fmt_str.format(
                    sr_no=idx+1,
                    registration_no=data["registration_no"],
                    colour=data["colour"]
                ))
        
        return "\n".join(result_set)









