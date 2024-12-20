import pytest
from employee import Employee

@pytest.fixture
def test_employee_instance():
    """ Create an instance of the Employee class for all tests """
    employee = Employee('John', 'Doe', 500000)
    return employee

def test_give_default_raise(test_employee_instance):
    """ Test that a default raise works properly """
    # employee = Employee('John', 'Doe', 500000)
    test_employee_instance.give_raise()
    assert test_employee_instance.annual_salary == 505000

def test_give_custom_raise(test_employee_instance):
    """ Test that a custom raise works properly """
    # employee = Employee('John', 'Doe', 500000)
    test_employee_instance.give_raise(10000)
    assert test_employee_instance.annual_salary == 510000