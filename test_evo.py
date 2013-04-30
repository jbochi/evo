from evo import Evo

def test_evo_should_list_configs():
    server = Evo("127.0.0.1")
    response = server.listConfig()
    assert response['status'] == 'SUCCESS'
