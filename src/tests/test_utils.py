from src.utils import get_split_line


def test_get_split_line():

    test_line = 'I, like, Python'
    split_line = get_split_line(test_line)

    split_line[0] == 'I'
    split_line[1] == 'like'
    split_line[2] == 'Python'



