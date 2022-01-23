import numpy as np
import math
import array
import matplotlib.pyplot as plt
import pandas as pd


class Data:
    def __init__(self , data_array):
        self.array = data_array

    def initiziale(self , time , sza , id):
        self.time = time
        self.id = id
        self.sza = sza





def get_data_from_both_files(array_numberD , array_numberG):
    final_array_before_return = np.array ( [["Time" , "sza" , "ID-D" , "ID-G" , "I-diff"]] )

    counter = 1
    while True:
        if array_numberD.id[counter]>0 and array_numberG.id[counter] > 0 and array_numberD.sza[counter] < 88 and array_numberG.sza[counter] < 88:
            i_diff = array_numberG.id[counter] - ((array_numberD.id[counter]) * math.cos (array_numberD.sza[counter] * math.pi / 180 ))

            tmp = np.array ( [[array_numberD.time[counter] , array_numberD.sza[counter] , array_numberG.id[counter] , array_numberD.id[counter] , i_diff]] )
            final_array_before_return = np.concatenate ( (final_array_before_return , tmp) , axis=0 )

        counter = counter + 1
        if counter >= array_numberD.array.shape[0] - 1:
            break

    return final_array_before_return


if __name__ == "__main__":

    def appender(number):
        my_string = ''
        if number // 10 == 0:
            my_string = "00" + str ( number )
        elif number // 100 == 0:
            my_string = "0" + str ( number )
        else:
            my_string = str ( number )
        return my_string


    for x in range ( 1 , 367 ):

        i_diff_ = 0
        i_diff_sum = 0

        if x != 24 and x != 23 and x != 22 and x!=111:
            key = appender ( x )

            pathD = "C:/Users/Lavdi/Desktop/DIRECT_2016-2019/2016/DIR" + key + "16.DAT"
            pathG = "C:/Users/Lavdi/Desktop/GLB_2016-2019/2016/TOT" + key + "16.DAT"

            with open ( pathD , 'r' ) as D:
                datad = Data ( np.genfromtxt ( D , delimiter='' ) )
                np.set_printoptions ( formatter={'float': '{: 0.3f}'.format} )

                datad.initiziale ( datad.array[: , ][1: , 0] , datad.array[: , ][1: , 1] , datad.array[: , ][1: , 2] )

                # print("We deleted in total " + str(count_errors) + " incorrect or unreliable data")

            with open ( pathG , 'r' ) as G:
                datag = Data ( np.genfromtxt ( G , delimiter='' ) )
                np.set_printoptions ( formatter={'float': '{: 0.3f}'.format} )

                datag.initiziale ( datag.array[: , ][1: , 0] , datag.array[: , ][1: , 1] , datag.array[: , ][1: , 2] )

            final_array = get_data_from_both_files ( datad , datag )





            for items in range ( 1 , final_array.shape[0] ):
                i_diff_sum = i_diff_sum + float ( final_array[items][4] )

            i_diff_ = i_diff_sum*(0.0167)



            print(key + "," + str(i_diff_))


