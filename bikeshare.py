# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 12:13:57 2021

@author: Egina Malaj
@contact: eginamalaj@gmail.com
"""

# Packages that need to be imported
import time
import pandas as pd
import numpy as np
import calendar

# Get data
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Functions
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please enter a city name: Chicago, New York City or Washington! - ")
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("\nCity not in the list\n")
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please select month: January, Feburary, March, April, May or June or select All for all months - ")
        month = month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Month not in the list")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please select the day of the week: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday or select All for all days- ")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Invalid Day of the week")
    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1


        df = df[df['month'] == month]


    if day != 'all':


        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month= df['month'].mode()[0]
    common_month = calendar.month_name[common_month]
    print(common_month, "is the most common month.")

    # display the most common day of week
    print(df['day_of_week'].mode()[0], "is the most common day of week.")

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print(df['hour'].mode()[0], "hrs is the most common start hour.")

    print("\nThis took %s seconds to run." % (round(time.time() - start_time,4)))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(df['Start Station'].mode()[0], "is the most commonly used start station.", )

    # display most commonly used end station
    print(df['End Station'].mode()[0], "is the most commonly used end station.")

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station']
    print(df['combination'].mode()[0], "is the most frequent combination of start station and end station trip, respectively.")

    print("\nThis took %s seconds to run." % (round(time.time() - start_time,4)))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(df['Trip Duration'].sum(), "is the total travel time for your selection.")

    # display mean travel time
    trip_duration = df['Trip Duration'].mean()
    print(round(trip_duration,2), "is the total mean time for your selection.")

    print("\nThis took %s seconds to run." % (round(time.time() - start_time,4)))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count = df.groupby(['User Type'])['User Type'].count()
    print(user_count, "\n")

    if city != 'washington':
        # Display counts of gender
        gender = df.groupby(['Gender'])['Gender'].count()
        print(gender)
        # Display earliest, most recent, and most common year of birth
        earliest = int(sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0])
        recent = int(sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0])
        common = int(df['Birth Year'].mode()[0])
        print(earliest, "is the earliest year of birth")
        print(recent, "is the most recent year of birth")
        print(common, "is the most common year of birth")

    print("\nThis took %s seconds to run." % (round(time.time() - start_time,4)))

    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
