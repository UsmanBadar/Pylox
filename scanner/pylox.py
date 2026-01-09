import sys


class PyLox:

    had_error = False


    @staticmethod
    def report(line_number, where, message):
        PyLox.had_error = True
        # Where functionality not implemented yet
        sys.stderr.write(f"[line {line_number}] Error{where}: {message}\n")


    @staticmethod   
    def error(line, message):
        PyLox.had_error = True
        PyLox.report(line, "", message)
