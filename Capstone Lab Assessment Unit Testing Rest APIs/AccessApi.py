import AccessApi as mws
import pytest

#base_url: str = "https://raw.githubusercontent.com/bclipp/"
base_url: str = "https://raw.githubusercontent.com/cengage-ide-content/"
billing_end_point: str = "APItesting/master/getBillingInfo.json"
customer_end_point: str = "APItesting/master/getCustomers.json"
site_end_point: str = "APItesting/master/getSites.json"

# TASK 2

# billing
def test_billing_status_code(base_url: str, end_point: str):
    url = mws.AccessApi(base_url)
    status_code = url.get_status_code(billing_end_point)
    assert status_code == 200

def test_billing_validate_schema():
    url = mws.AccessApi(base_url)
    billing_text = url.get_end_point(billing_end_point)
    k = ['id', 'FirstName', 'LastName', 'city', 'state', 'Lang', 'SSN']
    for pair in billing_text:
        assert list(pair.keys()) == k
        for item in pair.items():
            if item[0] == 'id':
                assert type(item[1]) is int
            else:
                assert type(item[1]) is str

def test_billing_validate_ssn():
    url = mws.AccessApi(base_url)
    billing_text = url.get_end_point(billing_end_point)
    for each in billing_text:
        ssn = each.get('SSN')
        onlynum = ssn.replace('-', '')
        assert ssn.index('-') == 3
        assert ssn.rindex('-') == 6
        assert onlynum.isdecimal() == True
    return True

def test_billing_validate_time():
    url = mws.AccessApi(base_url)
    elapsed_time = url.get_elapsed_time(billing_end_point)
    assert elapsed_time < 1


# customers
def test_customers_status_code():
    url = mws.AccessApi(base_url)
    status_code = url.get_status_code(customer_end_point)
    assert status_code == 200

def test_customers_validate_schema():
    url = mws.AccessApi(base_url)
    customers_text = url.get_end_point(customer_end_point)
    k = ['id', 'first_name', 'last_name', 'email', 'ip_address', 'address']
    for pair in customers_text:
        assert list(pair.keys()) == k
        for item in pair.items():
            if item[0] == 'id':
                assert type(item[1]) is int
            else:
                assert type(item[1]) is str

def test_customers_validate_ssn():
    url = mws.AccessApi(base_url)
    customers_text = url.get_end_point(customer_end_point)
    for each in customers_text:
        email = each.get('email')
        email_username = email.split('@', 1)[0]
        email_service = email.split('@', 1)[1]
        assert email.count('@') == 1
        #assert email_service.count('.') == 1
        #assert email_service.index('.') == -4
        assert type(email) == str
    return True

def test_customers_validate_time():
    url = mws.AccessApi(base_url)
    elapsed_time = url.get_elapsed_time(customer_end_point)
    assert elapsed_time < 1

# site
def test_site_status_code():
    url = mws.AccessApi(base_url)
    status_code = url.get_status_code(site_end_point)
    assert status_code == 200

def test_site_validate_schema():
    url = mws.AccessApi(base_url)
    site_text = url.get_end_point(site_end_point)
    k = ['id', 'address', 'ThirdParty', 'admin']
    for pair in site_text:
        assert list(pair.keys()) == k
        for item in pair.items():
            if item[0] == 'id':
                assert type(item[1]) is int
            else:
                assert type(item[1]) is str

def test_site_validate_ssn():
    url = mws.AccessApi(base_url)
    site_text = url.get_end_point(site_end_point)
    for each in site_text:
        id = each.get('id')
        assert type(id) == int
    return True

def test_site_validate_time():
    url = mws.AccessApi(base_url)
    elapsed_time = url.get_elapsed_time(site_end_point)
    assert elapsed_time < 1


# task 3
@pytest.mark.parametrize('base_url', [base_url])
@pytest.mark.parametrize('end_point', [billing_end_point, customer_end_point, site_end_point])

def test_billing_status_code(base_url, end_point):
    url = mws.AccessApi(base_url)
    for point in end_point:
        status_code = url.get_status_code(end_point)
        assert status_code == 200

@pytest.mark.parametrize('base_url', [base_url])
@pytest.mark.parametrize('end_point',[billing_end_point,customer_end_point,site_end_point])

def test_billing_validate_time(base_url, end_point):
    url = mws.AccessApi(base_url)
    for point in end_point:
        elapsed_time = url.get_elapsed_time(end_point)
        assert elapsed_time < 1
