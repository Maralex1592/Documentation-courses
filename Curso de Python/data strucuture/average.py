# -*- coding: utf-8 -*- 

def main(temps):
    sum_temps = 0

    for i in temps:
        sum_temps += float(i)

    return(sum_temps/len(temps)) 

if __name__ == '__main__':

    temps = [45,29,78,45,35,65,73,49,24]
    average = main(temps)

    print(average)