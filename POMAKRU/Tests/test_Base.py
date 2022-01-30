import pytest
import sys

@pytest.mark.usefixtures("init__driver")
class BaseTest:
    pass