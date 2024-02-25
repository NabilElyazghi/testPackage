from mypackage import mymodule

def test_top_n():
    """
    make sure top_n works correctly
    """

    assert mymodule.top_n([3,7,6,2,5],2)==[2,3],'incorrect'
    assert mymodule.top_n([-1,-8,6,2,5],3)==[-8,-1,2],'incorrect'