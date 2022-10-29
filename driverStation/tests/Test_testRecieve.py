
target = __import__("my_sum.py") #  

def test_sum():
    
    assert sum([1, 2, 3]) == 6, "Should be 6"

