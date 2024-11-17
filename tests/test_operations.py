from src.math_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(4,3)==7
    assert add(5,4)==9

def test_sub():
    assert sub(10,4)==6
    assert sub(5,2)==3
    assert sub(7,5)==2