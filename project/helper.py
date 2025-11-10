


def to_hex(rgb_value):
    return "#"+hex(rgb_value[0])[2:]+hex(rgb_value[1])[2:]+hex(rgb_value[2])[2:]


def progress_bar(length, percent):
    bar = ""
    for i in range(length):
        if percent > i/length*100:
            bar += "#"
        else:
            bar += "-"
    return str(round(percent))+" "+bar+" 100%"