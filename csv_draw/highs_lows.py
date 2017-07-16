import csv
from matplotlib import pyplot as plt
from datetime import datetime


def sitka_month():
    filename = 'sitka_weather_07-2014.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        # for index, column in enumerate(header_row):
        #     print(index, column)

        highs = []
        dates = []
        for row in reader:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            highs.append(high)
            dates.append(current_date)

        # draw
        plt.plot(dates, highs, c='red')
        plt.title('Daily High temperature,July 2014', fontsize=20)
        plt.xlabel('Date', fontsize=16)
        plt.ylabel('Temperature (F)', fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()


def sitaka_year():
    filename = 'sitka_weather_2014.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)

        dates = []
        lows = []
        highs = []
        for row in reader:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.fill_between(dates, lows, highs, facecolor='blue', alpha=0.1)
    plt.title('Daily temperature 2014', fontsize=20)
    plt.xlabel('Date', fontsize=16)
    plt.ylabel('Temperature(F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()


def valley_year():
    filename = 'death_valley_2014.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)

        dates = []
        lows = []
        highs = []

        for row in reader:
            try:
                current_date = datetime.strptime(row[0], '%Y-%m-%d')
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print('Missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

        plt.plot(dates, lows, c='blue', alpha=0.5)
        plt.plot(dates, highs, c='red', alpha=0.5)
        plt.fill_between(dates, lows, highs, facecolor='blue', alpha=0.1)
        plt.title('daily temperature 2014 of valley', fontsize=16)
        plt.xlabel('Date', fontsize=16)
        plt.ylabel('Temperature(F)', fontsize=16)
        plt.show()


# sitka_month()
# sitaka_year()
valley_year()
