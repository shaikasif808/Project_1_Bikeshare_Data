#!/usr/bin/env python
# coding: utf-8

# # Project 1
# ## Explore US Bikeshare Data
# Following project provide the statics about bikesharing system in 3 major cities of United States. Data has been provided by Udacity platform for:
# **__Chicago__**, **__New York City__** and **__Washington DC__**.
# The data has been wrangled already wrangled and shared in a form of CSV file for each city separtely

# In[ ]:


# In[39]:


# directories that need to be imported

import time
import statistics
import pandas as pd
import numpy as np
import sys


# In[40]:


# function to apply the respective filters from user

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = "all"
    month = "all"
    day = "all"

    citys = ['Chicago', 'New York City', 'Washington']
    count = 0
    # it will help to redirect the user untill he/she enters a correct input
    while city not in citys:
        if count < 15:
            print("Select only Chicago, New York City, or Washington")
        else:
            print("Sorry... your attempts exceed the premitted one")
            sys.exit()
        city = input("Which city stats are you intreseted in: \n").title()
        count += 1

    filter_ans = input("How do you want to filter data like wrt to month, day, both, or none: \n")

    count = 0
    if filter_ans == "month":
        months = ["Jan", "Feb", "March", "Apiril", "May", "June"]
        while month not in months:
            if count < 15:
                print("Enter a month from suggested abbrevitions")
            else:
                # a specified count is provided to break a while loop
                print("Sorry... your attempts exceed the premitted one")
                sys.exit()
            month = input("Select a month from Jan, Feb, March, Apiril, May, or June: \n").title()
            count += 1
    elif filter_ans == "day":
        days = ["Mon", "Tue", "Wed", "Thrus", "Fri", "Sat", "Sun"]
        while day not in days:
            if count < 15:
                print("Enter a day from suggested abbvrevitions")
            else:
                print("Sorry... your attempts exceed the premitted one")
                sys.exit()
            day = input("Select a day from Mon, Tue, Wed, Thrus, Fri, Sat or Sun: \n").title()
            count += 1
    elif filter_ans == "both":
        months = ["Jan", "Feb", "March", "Apiril", "May", "June"]
        while month not in months:
            if count < 15:
                print("Please enter a month from suggested abvrevitions")
            else:
                print("Sorry... your attempts exceed the premitted one")
                sys.exit()
            month = input("Select a month from Jan, Feb, March, Apiril, May, or June: \n").title()
            count += 1
        count = 0
        days = ["Mon", "Tue", "Wed", "Thrus", "Fri", "Sat", "Sun"]
        while day not in days:
            if count < 15:
                print("Please enter a day from suggested abvrevitions")
            else:
                print("Sorry... your attempts exceed the premitted one")
                sys.exit()
            day = input("Select a day from Mon, Tue, Wed, Thrus, Fri, Sat or Sun: \n").title()
            count += 1
    else:
        print("Presenting overall stats:")

    print('-' * 100)
    return city, month, day


# In[41]:


# function to load the data from csv files provided as input

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print("Loading the data and it's super fast........")
    CITY_DATA = {'Chicago': 'chicago.csv',
                 'New York City': 'new_york_city.csv',
                 'Washington': 'washington.csv'}

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month, day and hour of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour

    # filter data based on months
    if month != "all":
        months = ["Jan", "Feb", "March", "Apiril", "May", "June"]
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter data based on days
    if day != "all":
        days = ["Mon", "Tue", "Wed", "Thrus", "Fri", "Sat", "Sun"]
        day = days.index(day)
        df = df[df['day_of_week'] == day]

    print("Yo!!! The data has been loaded")

    print('-' * 100)

    return df


# In[42]:


# function to get the time statatics

def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel.
    INPUT:
    data frame of bikeshare data with or without filter
    OUTPUT:
    no return statement
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months = ["Jan", "Feb", "March", "Apiril", "May", "June"]
    days = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"]

    # If a user provides the month and day than it suppose to be the most common month and day and hence
    # it doesn't make sense to consider them most common
    if month == "all" and day == "all":
        max_month = df["month"].value_counts().idxmax()
        print("The most common month sharebike commutators travelled is: {}".format(months[max_month - 1]))
        max_day = df["day_of_week"].value_counts().idxmax()
        print("The most common day sharebike commutators travelled is: {}".format(days[max_day]))
    # If a user provides a month than it suppose to be the most common month
    # hence we can get most common day in that month
    elif month != "all" and day == "all":
        max_day = df["day_of_week"].value_counts().idxmax()
        print("The most common day sharebike commutators travelled is: {}".format(days[max_day]))
    # If a user provides a day than it suppose to be the most common day
    # hence we can get most common month in that day
    elif day != "all" and month == "all":
        max_month = df["month"].value_counts().idxmax()
        print("The most common month sharebike commutators travelled is: {}".format(months[max_month - 1]))

    # display the most common start hour
    max_hour = df["hour"].value_counts().idxmax()
    print("The most rush hour is: {}".format(max_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 100)


# In[43]:


# function to get the station statatics

def station_stats(df, city, month, day):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    if month != "all" and day != "all":
        start_station = df['Start Station'].value_counts().idxmax()
        print("The most commonly used start station during {}'s in {} is: {}".format(day, month, start_station))
    elif month != "all":
        start_station = df['Start Station'].value_counts().idxmax()
        print("The most commonly used start station in {} month is: {}".format(month, start_station))
    elif day != "all":
        start_station = df['Start Station'].value_counts().idxmax()
        print("The most commonly used start station on {}'s is: {}".format(day, start_station))
    else:
        start_station = df['Start Station'].value_counts().idxmax()
        print("The most commonly used start station is: {}".format(start_station))

    # display most commonly used end station
    if month != "all" and day != "all":
        end_station = df['End Station'].value_counts().idxmax()
        print("The most commonly used end station during {}'s in {} is: {}".format(day, month, end_station))
    elif month != "all":
        end_station = df['End Station'].value_counts().idxmax()
        print("The most commonly used end station in {} month is: {}".format(month, end_station))
    elif day != "all":
        end_station = df['End Station'].value_counts().idxmax()
        print("The most commonly used end station on {}'s is: {}".format(day, end_station))
    else:
        end_station = df['End Station'].value_counts().idxmax()
        print("The most commonly used end station is: {}".format(end_station))

    # display most frequent combination of start station and end station trip
    if month != "all" and day != "all":
        start_end_station = df.groupby(['Start Station', 'End Station']).size().idxmax()
        print('''The most frequent combination of start station and end station trip during {}'s in {} is: 
                 start station: {} \
                 end station: {}'''.format(day, month, start_end_station[0], start_end_station[1]))
    elif month != "all":
        start_end_station = df.groupby(['Start Station', 'End Station']).size().idxmax()
        print('''The most frequent combination of start station and end station in {} month is: 
                 start station: {} \
                 end station: {}'''.format(month, start_end_station[0], start_end_station[1]))
    elif day != "all":
        start_end_station = df.groupby(['Start Station', 'End Station']).size().idxmax()
        print('''The most frequent combination of start station and end station during {}'s is: 
                 start station: {} \
                 end station: {}'''.format(day, start_end_station[0], start_end_station[1]))
    else:
        start_end_station = df.groupby(['Start Station', 'End Station']).size().idxmax()
        print('''The most frequent combination of start station and end station are: 
                 start station: {}
                 end station: {}'''.format(start_end_station[0], start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 100)


# In[44]:


# function to get the trip duration statatics

def trip_duration_stats(df, city, month, day):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    if month != "all" and day != "all":
        trip_duration = pd.to_numeric(df['Trip Duration'])
        print("The entire trip duration during {}'s in {} is: {} Hours.".format(day, month,
                                                                                round((trip_duration.sum()) / 3600, 2)))
    elif month != "all":
        trip_duration = pd.to_numeric(df['Trip Duration'])
        print(
            "The entire trip duration in {} month is: {} Hours.".format(month, round((trip_duration.sum()) / 3600, 2)))
    elif day != "all":
        trip_duration = pd.to_numeric(df['Trip Duration'])
        print("The entire trip duration during {}'s is: {} Hours.".format(day, round((trip_duration.sum()) / 3600, 2)))
    else:
        trip_duration = pd.to_numeric(df['Trip Duration'])
        print("The entire trip duration is: {} Hours.".format(round((trip_duration.sum()) / 3600, 2)))

    # display mean travel time
    if month != "all" and day != "all":
        trip_duration = pd.to_numeric(df['Trip Duration'])
        print("The mean trip duration during {}'s in {} is: {} Mins.".format(day, month,
                                                                             round((trip_duration.mean()) / 60, 2)))
    elif month != "all":
        trip_duration = pd.to_numeric(df['Trip Duration'])
        print("The mean trip duration in {} month is: {} Mins.".format(month, round((trip_duration.mean()) / 60, 2)))
    elif day != "all":
        trip_duration = pd.to_numeric(df['Trip Duration'])
        print("The mean trip duration during {}'s is: {} Mins.".format(day, round((trip_duration.mean()) / 60, 2)))
    else:
        trip_duration = pd.to_numeric(df['Trip Duration'])
        print("The mean trip duration is: {} Mins.".format(round((trip_duration.mean()) / 60, 2)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 100)


# In[ ]:


# function to get the user statatics

def user_stats(df, city, month, day):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    if month != "all" and day != "all":
        print("On {}'s in {} :".format(day, month))
        print("The number of {}'s is: {}".format(df['User Type'].value_counts().keys().tolist()[0], df['User Type'].value_counts().tolist()[0]))
        print("The number of {}'s is: {}".format(df['User Type'].value_counts().keys().tolist()[1], df['User Type'].value_counts().tolist()[1]))
        if "Dependent" in df['User Type'].value_counts().keys().tolist():
            print("The number of {}'s is: {}".format(df['User Type'].value_counts().keys().tolist()[2],
                                                     df['User Type'].value_counts().tolist()[2]))

    elif month != "all":
        print("In {} :".format(month))
        print("The number of {}'s is: {}".format(df['User Type'].value_counts().keys().tolist()[0], df['User Type'].value_counts().tolist()[0]))
        print("The number of {}'s is: {}".format(df['User Type'].value_counts().keys().tolist()[1], df['User Type'].value_counts().tolist()[1]))
        if "Dependent" in df['User Type'].value_counts().keys().tolist():
            print("The number of {}'s is: {}".format(df['User Type'].value_counts().keys().tolist()[2],
                                                     df['User Type'].value_counts().tolist()[2]))
    elif day != "all":
        print("On {}'s :".format(day))
        print("The number of {}'s is: {}".format(df['User Type'].value_counts().keys().tolist()[0], df['User Type'].value_counts().tolist()[0]))
        print("The number of {}'s is: {}".format(df['User Type'].value_counts().keys().tolist()[1], df['User Type'].value_counts().tolist()[1]))
        if "Dependent" in df['User Type'].value_counts().keys().tolist():
            print("The number of {}'s is: {}".format(df['User Type'].value_counts().keys().tolist()[2],
                                                     df['User Type'].value_counts().tolist()[2]))

    else:
        print("The number of {}'s is: {}".format(df['User Type'].value_counts().keys().tolist()[0], df['User Type'].value_counts().tolist()[0]))
        print("The number of {}'s is: {}".format(df['User Type'].value_counts().keys().tolist()[1], df['User Type'].value_counts().tolist()[1]))
        if "Dependent" in df['User Type'].value_counts().keys().tolist():
            print("The number of {}'s is: {}".format(df['User Type'].value_counts().keys().tolist()[2],
                                                     df['User Type'].value_counts().tolist()[2]))

    # Display counts of gender
    if city == 'Chicago' or city == 'New York City':
        if month != "all" and day != "all":
            print("On {}'s in {} :".format(day, month))
            print("The number of {}'s is: {}".format(df['Gender'].value_counts().keys().tolist()[0], df['Gender'].value_counts().tolist()[0]))
            print("The number of {}'s is: {}".format(df['Gender'].value_counts().keys().tolist()[1], df['Gender'].value_counts().tolist()[1]))
        elif month != "all":
            print("In {} :".format(month))
            print("The number of {}'s is: {}".format(df['Gender'].value_counts().keys().tolist()[0], df['Gender'].value_counts().tolist()[0]))
            print("The number of {}'s is: {}".format(df['Gender'].value_counts().keys().tolist()[1], df['Gender'].value_counts().tolist()[1]))
        elif day != "all":
            print("On {}'s :".format(day))
            print("The number of {}'s is: {}".format(df['Gender'].value_counts().keys().tolist()[0], df['Gender'].value_counts().tolist()[0]))
            print("The number of {}'s is: {}".format(df['Gender'].value_counts().keys().tolist()[1], df['Gender'].value_counts().tolist()[1]))
        else:
            print("The number of {}'s is: {}".format(df['Gender'].value_counts().keys().tolist()[0], df['Gender'].value_counts().tolist()[0]))
            print("The number of {}'s is: {}".format(df['Gender'].value_counts().keys().tolist()[1], df['Gender'].value_counts().tolist()[1]))
    else:
        print("Gender data is not available.....")

    # Display counts of DOB
    if city == 'Chicago' or city == 'New York City':
        print("D.O.B of youngest commutator is: {}".format(int(df["Birth Year"].min())))
        print("D.O.B of eldest commutator is: {}".format(int(df["Birth Year"].max())))
        print("most common D.O.B is: {}".format(int(df["Birth Year"].mode()[0])))
    else:
        print("Birth Year data is not available.....")

    # Display earliest, most recent, and most common year of birth

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 100)


# In[46]:


# main function to call the all neccessary functions

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, city, month, day)
        station_stats(df, city, month, day)
        trip_duration_stats(df, city, month, day)
        user_stats(df, city, month, day)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


# In[ ]:


# function with python variable name to avoid the implementation of main function while importing this file
if __name__ == "__main__":
    CITY_DATA = {'chicago': 'chicago.csv',
                 'new york city': 'new_york_city.csv',
                 'washington': 'washington.csv'}

    main()