import csv
import time


def read_weather(f):
    output = {}

    with open(f,newline='') as file:

        r = csv.reader(file, delimiter='\t')

        for one_line in r:
            year, month, day, city, country, high, low, precip = one_line

            country = country.strip()
            city = city.strip()

            output.setdefault(country, {}) 
            output[country].setdefault(city, [])

            t = (int(year), int(month), int(day), int(high), int(low), int(precip))
            output[country][city].append(t)

    return output


def collect_and_validate_questions(f):
    data = read_weather(f)
    
    raw_answer = input('What info would you like to know?'
                        + ' Options: d - between dates; k - country, c - city and country, u - averages, q - quit.  ')
    
    if raw_answer == 'd':
        raw_date = input('Please insert start and end date as in: DD-MM-YYYY, DD-MM-YYYY ')
        raw_date_list = raw_date.split(',')
        raw_start_date, raw_end_date = raw_date_list
        raw_end_date = raw_end_date.strip()
        start_date = time.strptime(raw_start_date, '%d-%m-%Y')
        end_date = time.strptime(raw_end_date, '%d-%m-%Y')
        return('d', start_date, end_date)
    
    elif raw_answer == 'k':
        raw_country = input('What country are you interested in? ')
        if raw_country in data.keys():
            return ('k', raw_country)
        else:
            print('No data for such country')
    
    elif raw_answer == 'c':
        raw_city_contry = input('Please provide the city and country you are interested in, format: city, country ')
        city, country = raw_city_contry.split(',')
        country = country.strip()
        if country in data.keys():
            if city in data[country].keys():
                return('c', city, country)
            else:
                print('No city data')
        else:
            print('No country data')
        
    elif raw_answer == 'u':
        return 'u'

    elif raw_answer == 'q':
        return 'q'
    

def weather_data(f):
    data = read_weather(f)

    while True:
        request = collect_and_validate_questions(f)

        if request == 'q':
            break

        elif request == 'u':
            for country in data.keys():
                for city, city_data in data[country].items():
                    avg_max_temp = sum([record[3] for record in city_data]) / len (city_data)
                    avg_min_temp = sum([record[4] for record in city_data]) / len (city_data)
                    avg_prep = sum([record[5] for record in city_data]) / len (city_data)

                print(f'In {city} the average maximum temperature was {avg_max_temp},'
                        f'the average minimum temperature was {avg_min_temp},' 
                        f'and the average precipitation was {avg_prep}.')
        
        elif 'c' in request:
            answer, city, country = request
            print(f'Weather report for {city}, {country}:')
            for day_data in data[country][city]:
                print(f'On {day_data[2]}-{day_data[1]}-{day_data[0]}'
                        f' maximum temperature was {day_data[3]}, minimum temperature was {day_data[4]}, precipitations {day_data[5]}')
        
        elif 'k' in request:
            answer, country = request
            for city, city_data in data[country].items():
                print(f'Weather report for {city} in {country}:')
                for day_data in city_data:
                    print(f'On {day_data[2]}-{day_data[1]}-{day_data[0]}'
                        f' maximum temperature was {day_data[3]}, minimum temperature was {day_data[4]}, precipitations {day_data[5]}')

        elif 'd' in request:
            answer, start_date, end_date = request
            for country in data.keys():
                for city, city_data in data[country].items():
                    for day_data in city_data:
                        record_date = time.strptime(f'{day_data[2]}-{day_data[1]}-{day_data[0]}', '%d-%m-%Y')
                        if start_date <= record_date and end_date >= record_date:
                            print(f'On {day_data[2]}-{day_data[1]}-{day_data[0]}, in {city}, {country}'
                                    f' maximum temperature was {day_data[3]}, minimum temperature was {day_data[4]}, precipitations {day_data[5]}')
            
weather_data('weather_input.csv')