# Executive Dashboard Testing File

import pytest
from monthly_sales import to_usd

def test_to_usd():
    assert to_usd(23.50) == "$23.50"
    assert to_usd(2) == "$2.00"
    assert to_usd(1230.4) == "$1,230.40"