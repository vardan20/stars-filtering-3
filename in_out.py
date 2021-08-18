import star

'''
GetInput module organizes user input,
input(), show(), read_store() and write()
methods are implemented, which read and print user data,
store data in dictionary, and writes final form
in a new csv file
'''


class InputData:
    def __init__(self, ra, dec, fov_h, fov_v, n):
        self.ra = ra
        self.dec = dec
        self.fov_h = fov_h
        self.fov_v = fov_v
        self.n = n


def get_in() -> InputData:
    """takes all required input from user"""
    print("Please Enter equatorial coordinates, please separate them with a whitespace:", end=' ')
    ra, dec = map(float, input().split())
    print("Please Enter horizontal and vertical FOV, please separate them with a whitespace:", end=' ')
    fov_h, fov_v = map(float, input().split())
    n = int(input("Please Enter the number of Stars N: "))
    return InputData(ra, dec, fov_h, fov_v, n)
