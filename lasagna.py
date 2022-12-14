"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# TODO: define the 'EXPECTED_BAKE_TIME' constant
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(layers):
    """
    Calculate the total preparation time.
 
    :param layers: int - number of layers.
    :return: int - total time of preparation for all layers.
 
    Function that takes a number of lasagna layers, and returns how many minutes
    it needs to be prepared, based on the `PREPARATION_TIME`.
    """
    return layers*PREPARATION_TIME
    
    
# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(layers, bake_time):
    """
    Calculate the full time needed (preparation + baking) in minutes.
 
    :param layer: int - number of layers.
    :param bake_time: int - total baking time needed in minutes.
    :return: int - total time in minutes to prepare and bake the marvellous lasagna.
 
    Function that takes the preparation and baking times, and return the total in
    minutes.
    """
    return preparation_time_in_minutes(layers) + bake_time