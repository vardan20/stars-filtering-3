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
    while True:
        try:
            print("Please Enter equatorial coordinates, please separate them with a whitespace:", end=' ')
            ra, dec = map(float, input().split())
            print("Please Enter horizontal and vertical FOV, please separate them with a whitespace:", end=' ')
            fov_h, fov_v = map(float, input().split())
            n = int(input("Please Enter the number of Stars N: "))
            return InputData(ra, dec, fov_h, fov_v, n)
        except:
            print("Wrong Input Format, Please try again")


def read_store(dct: list, filename: str, ra: float, dec: float, fov_h: float, fov_v: float) -> tuple:
    """
    The read_store() method takes a filename as a parameter,
    and stores the information of that file in a
    dictionary.
    """
    star_cnt = 0
    with open(filename) as fd:
        id_n = 0
        for i in fd:
            item = i.split('\t')
            if id_n == 0:
                id_n += 1
                continue

            elif id_n == 1:
                dct = []
            else:
                """d1 is the RA distance between the given coordinate and i-th star"""
                d1 = abs(float(item[0]) - ra)
                if d1 > 180:
                    d1 = 360 - d1
                """d2 is the DEC distance between the given coordinate and i-th star"""
                d2 = abs(float(item[1]) - dec)
                """this two if-statements check if i-th star is in FOV or not"""
                if d1 > fov_h / 2:
                    id_n += 1
                    continue
                if d2 > fov_v / 2:
                    id_n += 1
                    continue
                cur = star.Star(float(item[0]), float(item[1]), id_n-2, float(item[7]), float(item[22]),0)

                dct.append(cur)
                star_cnt += 1

            id_n += 1

    return tuple([dct, star_cnt])


def write(table: dict, n: int, filename: str) -> None:
    """
    write method take data from the filtered table and
    writes it in filename.csv file
    """

    with open(filename, 'w') as f:
        row = ['id', 'source_id', 'ra_ep2000', 'dec_ep2000', 'phot_g_mean_mag', 'angular_distance']
        for i in row[:-1]:
            f.write(i+',')
        f.write(row[-1])
        f.write('\n')
        for i in range(n):
            row = [table[i].ind, table[i].source_id,
                   table[i].ra, table[i].dec,
                   table[i].phot_g_mean_mag, table[i].dist]
            for j in row[:-1]:
                f.write(str(j)+',')
            f.write(str(row[-1]))
            f.write('\n')
