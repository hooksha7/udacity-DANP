## TODO: import all necessary packages and functions
#import calendar
#import datetime
#import calendar
import pandas as pd
import time


## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

def get_city():
    global chicago, new_york_city, washington
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    # TODO: handle raw input and complete function
    rtn = None
    if city == 'Chicago':
        return chicago
    elif city == 'New York':
        return new_york_city
    elif city == 'Washington':
        return washington
    else:
        print('Wrong city')
        return get_city()


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')

    # TODO: handle raw input and complete function
    if time_period == 'month':
        return time_period
    elif time_period == 'day':
        return time_period
    elif time_period == 'none':
        return time_period
    else:
        print('Wrong time_period')
        return get_time_period()


def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    # TODO: handle raw input and complete function
    months = { 'January' : 1, 'February' : 2, 'March' : 3, 'April' : 4, 'May' : 5, 'June' : 6}

    if months in month:
        return months[month]
    else:
        print('Wrong month')
        return get_month()


def get_day(month):
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    day = input('\nWhich day? Please type your response as an integer.\n')

    # TODO: handle raw input and complete function
    if day == 'Monday':
        return 0
    elif day == 'Tuesday':
        return 1
    elif day == 'Wednesday':
        return 2
    elif day == 'Thursday':
        return 3
    elif day == 'Friday':
        return 4
    elif day == 'Saturday':
        return 5
    elif day == 'Sunday':
        return 6
    else:
        print("Wrong day, example : Monday")
    return get_day()

def popular_month(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    '''
    # TODO: complete function
    df = pd.read_csv(city_file)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Start Time_month'] = df['Start Time'].dt.month
    #print(df.groupby('Start Time_month').describe())
    #print(df['Start Time_month'].mode())
    print('popular_month ' + city_file + ' time_period ' + time_period)
    print(df['Start Time_month'].mode()[0])



def popular_day(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    # TODO: complete function
    df = pd.read_csv(city_file)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Start Time_day'] = df['Start Time'].dt.day
    #print(df.groupby('Start Time_day').describe())
    #print(df['Start Time_day'].mode())
    print('popular_day ' + city_file + ' time_period ' + time_period)
    print(df['Start Time_day'].mode()[0])



def popular_hour(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    '''
    # TODO: complete function
    df = pd.read_csv(city_file)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Start Time_hour'] = df['Start Time'].dt.hour
    #print(df.groupby('Start Time_hour').describe())
    #print(df['Start Time_hour'].mode())
    print('popular_hour ' + city_file + ' time_period ' + time_period)
    print(df['Start Time_hour'].mode()[0])


def trip_duration(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''
    # TODO: complete function
    df = pd.read_csv(city_file)
    total_trip_duration = df['Trip Duration'].sum()
    average_trip_duration = df['Trip Duration'].mean()
    print('trip_duration ' + city_file + ' time_period ' + time_period)
    print('total_trip_duration ' + str(total_trip_duration))
    print('average_trip_duration ' + str(average_trip_duration))


def popular_stations(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
    '''
    # TODO: complete function
    df = pd.read_csv(city_file)
    most_popular_start_station = df['Start Station'].mode()[0]
    most_popular_end_station = df['End Station'].mode()[0]
    print(df['Start Station'].describe())
    print(df['End Station'].describe())
    print('popular_stations ' + city_file + ' time_period ' + time_period)
    print('most_popular_start_station ' + most_popular_start_station)
    print('most_popular_end_station ' + most_popular_end_station)


def popular_trip(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    '''
    # TODO: complete function
    df = pd.read_csv(city_file)

    print('popular_trip ' + city_file + ' time_period ' + time_period)
    #begin 첫번째 방법
    most_popular_trip = df.groupby(['Start Station', 'End Station']).size().reset_index(name='start_end_station')
    max = most_popular_trip['start_end_station'].max()
    print('first')
    print(most_popular_trip.head())
    print(max)
    #end

    #begin 두번째 방법
    df['journey'] = df['Start Station'].str.cat(df['End Station'])
    #count = df['journey'].size()
    print('second')
    #print(df['journey'])
    print(df.groupby('journey').size().max())
    #end


def users(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    # TODO: complete function
    df = pd.read_csv(city_file)
    user_type = df['User Type'].drop_duplicates()
    print(user_type)
    user_type = df['User Type'].drop_duplicates().reset_index(name='user_type');
    print(user_type)
    user_type = user_type['user_type']
    print(user_type)
    np_user_type = user_type.values
    print(np_user_type)


def gender(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    '''
    # TODO: complete function
    df = pd.read_csv(city_file)
    gender = df.groupby('Gender').size()
    print('gender ' + city_file + ' time_period ' + time_period)
    print(gender)
    # CSV파일 열어보면, Gener에 빈칸인 경우가 있던대... 일단 패스.
    # washinton.csv 파일에는 Gender 컬럼이 없네요


def birth_years(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    '''
    # TODO: complete function
    print('birth_years ' + city_file + ' time_period ' + time_period)
    df = pd.read_csv(city_file)
    birth_year = df['Birth Year']
    min = birth_year.min()
    max = birth_year.max()
    mose_popular = birth_year.mode()[0]
    print('min ' + str(min))
    print('max ' + str(max))
    print('mose_popular ' + str(mose_popular))


def display_data(city_file):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    # TODO: handle raw input and complete function
    if display.lower() == 'yes':
        df = pd.read_csv(city_file)
        print(df.head())

def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()
        
        #TODO: call popular_month function and print the results
        popular_month(city, time_period)
        
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        
        # TODO: call popular_day function and print the results
        popular_day(city, time_period)
        
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")    

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
    popular_hour(city, time_period)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    trip_duration(city, time_period)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    popular_stations(city, time_period)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
    popular_trip(city, time_period)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results
    users(city, time_period)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results
    gender(city, time_period)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results
    birth_years(city, time_period)

    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data(city)


if __name__ == "__main__":
    while True:
        statistics()
        # Restart?
        restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
        if restart.lower() != 'yes':
            break



