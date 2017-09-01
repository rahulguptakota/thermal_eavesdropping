import sensors
import matplotlib.pyplot as plt

i = 0
sensors.init()

def get_thermal_data():
    data = {}
    for chip in sensors.iter_detected_chips():
        # print(chip, chip.adapter_name)
        for feature in chip:
            data[feature.label] = feature.get_value()
            print(feature.label, feature.get_value())
    return data

def plot():
    global i
    # plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
    while True:
        i = i+1
        data = get_thermal_data()
        j=0
        for (key,value) in data.items():
            j = j + 1
            plt.scatter(i, value, linewidths=1)
            break
        plt.pause(0.2)


plot()


# while(1):

