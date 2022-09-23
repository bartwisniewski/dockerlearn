from flask import Flask, request

PATH = "./static/parameters.txt"

app = Flask(__name__)


def write_arguments(arguments: list) -> None:
    length = len(arguments)
    if length == 0:
        return

    with open(PATH, 'a') as f:
        index = 0
        for argument in arguments:
            end_sign = "\n" if index+1 == length else ", "
            f.write(f"{argument[0]}: {argument[1]}"+end_sign)
            index += 1


@app.route('/')
def get_params():
    arguments = []
    for key in request.args:
        arguments.append((key, request.args[key]))
    write_arguments(arguments)
    s = "s" if len(arguments) != 1 else ""
    return f"get {len(arguments)} argument" + s


if __name__ == "__main__":
    app.run(host="0.0.0.0")
