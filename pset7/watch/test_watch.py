from watch import parse

def test_valid():
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse('<iframe width="560" src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"

def test_invalid():
    assert parse('<iframe src="https://vimeo.com/embed/xvFZjo5PgG0"></iframe>') == None
    assert parse("nothing here") == None
    assert parse('<iframe src="https://youtube.com/watch?v=xvFZjo5PgG0"></iframe>') == None