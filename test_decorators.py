from decorators import Colors, deco

def test_colors_constants():
    assert isinstance(Colors.RED, str)
    assert Colors.RESET == '\033[0m'

def test_deco_wraps_function_output(capsys):
    @deco("red")
    def say_hello():
        print("Hello")

    say_hello()
    captured = capsys.readouterr()
    assert "Hello" in captured.out
    assert "\033[91m" in captured.out  # red color
    assert "\033[0m" in captured.out   # reset
