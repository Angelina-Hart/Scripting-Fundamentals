import AccessApi as mws
import pytest

base_url: str = "https://raw.githubusercontent.com/bclipp/"
billing_end_point: str = "APItesting/master/getBillingInfo.json"
customer_end_point: str = "APItesting/master/getCustomers.json"
site_end_point: str = "APItesting/master/getSites.json"

# TASK 2

# billing
def test_billing_status_code():
    url = mws.AccessApi(url)
    status_code = url.get_status_code(end_point)
    assert status_code == 200

def test_billing_validate_schema():
    url = mws.AccessApi(url)
    billing_text = get_end_point(end_point)
    k = ['id', 'FirstName', 'LastName', 'city', 'state', 'Lang', 'SSN']
    assert list(billing_text.keys()) == k

def test_billing_validate_ssn():
    pass

def test_billing_validate_time():
    pass


# customers
def test_customers_status_code():
    pass

def test_customers_validate_schema():
    pass

def test_customers_validate_ssn():
    pass

def test_customers_validate_time():
    pass


# site
def test_site_status_code():
    pass

def test_site_validate_schema():
    pass

def test_site_validate_ssn():
    pass

def test_site_validate_time():
    pass

    
# task 3
@pytest.mark.parametrize('base_url', [base_url])
@pytest.mark.parametrize('billing_end_point', [billing_end_point, customer_end_point, site_end_point])


@pytest.mark.parametrize('base_url', [base_url])
@pytest.mark.parametrize('billing_end_point',[billing_end_point,customer_end_point,site_end_point])
def test_billing_validate_time(base_url,billing_end_point):
    pass
