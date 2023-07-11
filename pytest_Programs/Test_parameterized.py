import pytest


# @pytest.mark.parametrize("username,password",
#                          [
#                              ("asd", 'asdf@1010'),
#                              ("asdfg",'asd#15'),
#                              ("abc",'asjd@5'),
#                              ("dff",'sdv@54')
#                          ]
#                          )
# def test_login(username, password):
#     print(username + " " + password)
#
#     if(username == 'abc'):
#         assert False

@pytest.mark.parametrize("username,password",
                         [
                            ("asf","asdf@564"),
                            ("asdf","asdfg@56"),
                            ("hfjgh","afg@354"),
                            ("asdf","asdf@#54")
                         ]
                         )
def test_login(username,password):
    print((username + " "+ password))

    if (username== 'asf'):
        assert False