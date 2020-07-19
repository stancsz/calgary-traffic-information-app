def get_index(db_input, year_input):
    """
    get_index computes the GUI selection and return a [db type, collection name]
    to the function caller
    :param db_input:
    :param year_input:
    :return:
    """
    input_var = str(db_input) + '/' + str(year_input)
    switcher = {
        'volume/2016': '',
        'volume/2017': ['db_volume', '2017_traffic_volume_flow'],
        'volume/2018': '',
        'volume/2019': '',
        'volume/2020': '',
        'incidents/2016': '',
        'incidents/2017': '',
        'incidents/2018': '',
        'incidents/2019': '',
        'incidents/2020': '',
    }
    return_index = switcher.get(input_var, -1) # return -1 if index is not found
    return return_index


def test():
    print(get_index('volume', '2017'))
    print(get_index('volume', '2017')[0])
    print(get_index('volume', '2017')[1])
    return


if __name__ == '__main__':
    test()