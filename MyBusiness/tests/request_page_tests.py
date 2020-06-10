def test_request_answers(app):
    app.RequestPage.open_page()
    assert app.RequestPage.check_answer_labels() is True