
def test_creation_article(client,mocker):
    mocker_create = mocker.patch("src.Services.ArticlesDBService.createArticle")
    mocker_create.return_value = {
        "status":201,
        "message":"article created",
        "data":{"id ":1,"description":"testing","title":"testing"}
    }

    test_data = {"id ":1,"description":"testing","title":"testing"}

    response = client.post("/articles/",json=test_data)
    assert response.get_json() == {"id ":1,"description":"testing","title":"testing"}
    mocker_create.assert_called_once_with(test_data)