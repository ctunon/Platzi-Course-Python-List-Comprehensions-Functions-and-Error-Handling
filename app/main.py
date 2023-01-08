import utils
import read_csv
import charts


def run():
    data = read_csv.read_csv('./app/data.csv')
    data = list(filter(lambda item:item['Continent'] == 'North America', data))
    
    '''countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)'''
    
    try:
        result = utils.population_by_country(data, input('Type the country name: '))
        
        labels, values = utils.get_population(result[0])

        charts.generate_bar_chart(labels=labels, values=values)

    except IndexError:
        print('This country doesn´t exist in North America')





if __name__ == '__main__':
    run()