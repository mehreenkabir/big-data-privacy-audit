import pytest
from scripts.scan_reviews import find_pii

def test_email_detection():
    assert find_pii("Contact me at jane.doe@example.com") == 
["jane.doe@example.com"]

def test_ip_detection():
    assert find_pii("Server at 192.168.1.1 is down") == ["192.168.1.1"]

def test_both_pii():
    assert set(find_pii("Email: test@abc.com IP: 8.8.8.8")) == 
{"test@abc.com", "8.8.8.8"}

def test_no_pii():
    assert find_pii("No sensitive data here") == []

def test_empty_input():
    assert find_pii("") == []

def test_non_string():
    assert find_pii(12345) == []

def test_false_positive_version():
    assert find_pii("App version 1.2.3.4 is stable") == ["1.2.3.4"]

