import json
import pytest
from parking_lot.parking_lot import ParkingLot

MAX_LENGTH = 6

STATUS_OUTPUT = "Slot No.\tRegistration No\tColour\n1\tKA01HH1234\tWhite\n2\tKA01HH9999\tWhite\n3\tKA01BB0001\tBlack\n4\tKA01HH7777\tRed\n5\tKA01HH2701\tBlue\n6\tKA01HH3141\tBlack"

with open("./tests/test_data/allocation_data.json") as test_data_fp:
    allocation_data = json.load(test_data_fp)

with open("./tests/test_data/deallocation_data.json") as test_data_fp:
    deallocation_data = json.load(test_data_fp)

with open("./tests/test_data/queries_data.json") as test_data_fp:
    queries_data = json.load(test_data_fp)

parking_lot_obj = ParkingLot()


def test_intialization():

    output = parking_lot_obj.set_max_parking_slots(MAX_LENGTH) 

    assert output == "Created a parking lot with {max_len} slots".format(max_len =MAX_LENGTH)

def test_metadata():
    
    output = parking_lot_obj.get_metadata()

    assert output == "Max Slots: {max_len} | Free Slots {max_len} | Length: {max_len}".format(max_len=MAX_LENGTH)


@pytest.mark.parametrize("test_input", allocation_data)
def test_allocation(test_input):

    car_details = test_input["input"].split(" ")

    car_details_obj = {
        "registration_no":car_details[0],
        "colour":car_details[1]
    }

    output = parking_lot_obj.allocate_slot(car_details_obj)

    assert output == test_input["output"]


@pytest.mark.parametrize("test_input", queries_data)
def test_query(test_input):

    return_key, query_key, condition_value = test_input["input"].split(" ")

    output = parking_lot_obj.query(return_key, query_key, condition_value)

    assert output == test_input["output"]

def test_status():
    output = parking_lot_obj.status()

    assert output == STATUS_OUTPUT


@pytest.mark.parametrize("test_input", deallocation_data)
def test_deallocate_slot(test_input):

    slot = int(test_input["input"].strip())

    output = parking_lot_obj.deallocate_slot(slot)

    assert output == test_input["output"]