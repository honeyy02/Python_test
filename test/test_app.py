from my_app.app import add, sub

def test_add():
    assert add(5,4)==10
    assert add(8,2)==10

def test_sub():
    assert sub(4,2)==2
    assert sub(8,5)==3    