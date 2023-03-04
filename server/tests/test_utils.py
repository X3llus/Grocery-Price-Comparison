import math
import sys
sys.path.insert(0, '../')
# import utils
from utils import distance_between_coords, find_latitude_longitude_range, get_closest_store, format_loblaws_store


def test_distance_between_coords():
    x = distance_between_coords(10,11,12,12,"K")
    # used online calculator to calculate the distance between coordinates
    assert round(x) == 248 

def test_find_latitude_longitude_range():
    pass

def test_get_closest_store():
    pass

def test_format_loblaws_store():
    pass
