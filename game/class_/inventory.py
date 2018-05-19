from pprint import pprint


class InventoryHandler:
    def __init__(self, sizex, sizey):
        self.datas = [[None for i in range(sizey)] for i in range(sizey)]
        print(self.datas)

        print(self.datas)

    def sort_dict(self, dictionary):
        """
        sorts dictionary shaped like: {'1x2': whatever} and puts it into 
        the internal 2d list.
        """
        print(self.datas)
        for indexes in dictionary:
            x = int(indexes.split('x')[0])
            y = int(indexes.split('x')[1])
            #print(x, y)
            print("self.datas[{}][{}] = dictionary['{}']".format(
                x - 1, y - 1, indexes))
            self.datas[x - 1][y - 1] = dictionary[indexes]
            print(self.datas)


if __name__ == '__main__':
    a = InventoryHandler(2, 2)
    s = {
        '1x1': '0',
        '1x2': '1',
        '2x1': '2',
        '2x2': '3',
    }
    a.sort_dict(s)
    pprint(a.datas)
