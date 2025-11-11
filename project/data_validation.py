import os
import time
from helper import progress_bar

validation_type = "length"
data_file = "data.txt"

def validate(data, val_type):
    if val_type=="length":
        validate_length(data)

def validate_length(data):
    file_size = get_file_size(data)
    file = open(data_file, "r")
    validation_dict = {}
    starting_time = time.time()
    for line_num in range(file_size):
        line = file.readline()
        length = len(line.split(",")) / 2
        if length in validation_dict:
            validation_dict[length] += 1
        else:
            validation_dict[length] = 1
        log_progress(line_num+1, file_size, starting_time, validation_dict, val_type = "length")

def log_progress(value, max_value, starting_time, validation_dict, val_type):
    cur_time = time.time()
    output = ("_________Validating ("+validation_type+")_________")
    output += "\n"+(progress_bar(20, value/max_value*100))
    output += "\n"+("Progress: "+str(value)+"/"+str(max_value))
    output += "\n"+("__________________________________")
    output += "\n"+("Time Elapsed: "+str(round(cur_time-starting_time,3))+"s")
    output += "\n"+("__________________________________")
    if val_type == "length":
        output += "\n"+("Lengths: ")
        keys = list(validation_dict.keys())
        for key in sorted(keys):
            data_points = validation_dict[key]
            output += "\n"+(str(int(key))+": "+str(data_points)+" ("+"{:.0%}".format(data_points/value)+")")
    os.system('cls')
    print(output)



def get_file_size(data_file):
    file = open(data_file, "r")
    return sum(1 for _ in file)


validate(data_file, validation_type)