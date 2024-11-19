from name_function import get_formatted_name

def test_first_last_name():
    """ Do names like 'Srujan Kumar' work """
    formatted_name = get_formatted_name('srujan', 'kumar')
    assert formatted_name == 'Srujan Kumar'

def test_first_middle_last_name():
    """ Do names like 'Srujan Kumar Kottapally' work. """
    formatted_name = get_formatted_name('srujan', 'kottapally', 'kumar')
    assert formatted_name == 'Srujan Kumar Kottapally'