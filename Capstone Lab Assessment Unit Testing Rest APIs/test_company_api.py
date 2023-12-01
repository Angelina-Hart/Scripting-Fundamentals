from functions import AccessApi as mws
import pytest

base_url: str = "https://raw.githubusercontent.com/bclipp/"
billing_end_point: str = "APItesting/master/getBillingInfo.json"
customer_end_point: str = "APItesting/master/getCustomers.json"
site_end_point: str = "APItesting/master/getSites.json"

# TASK 2

# billing
def test_billing_status_code():

def test_billing_validate_schema():

def test_billing_validate_ssn():

def test_billing_validate_time():


# customers
def test_customers_status_code():

def test_customers_validate_schema():

def test_customers_validate_ssn():

def test_customers_validate_time():


# site
def test_site_status_code():

def test_site_validate_schema():

def test_site_validate_ssn():

def test_site_validate_time():

    
# task 3
@pytest.mark.parametrize('base_url', [base_url])
@pytest.mark.parametrize('billing_end_point', [billing_end_point, customer_end_point, site_end_point])


@pytest.mark.parametrize('base_url', [base_url])
@pytest.mark.parametrize('billing_end_point',[billing_end_point,customer_end_point,site_end_point])
def test_billing_validate_time(base_url,billing_end_point):

