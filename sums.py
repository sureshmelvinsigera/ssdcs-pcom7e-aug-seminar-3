# SOURCE OF CODE: https://realpython.com/python-testing/


def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")

#1 pip install pytest-mccabe
#2 pytest -q --mccabe module.py
#3 ==>> 2 passed in 0.32s

# python -m mccabe --min 5 mccabe.py