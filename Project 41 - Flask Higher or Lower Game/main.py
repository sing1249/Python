import random
from flask import Flask
import random
app = Flask(__name__)


@app.route("/")
def guess_home():
    return '<h1>Guess a number between 0 and 9</h1>' \
            '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3VyZnV2cndocDhnYWoyeHRmYTd1cnhrbTNhd2h2YWpkbmUwOHM2MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Rs2QPsshsFI9zeT4Kn/giphy.webp" width = 300px>'

random_number = random.randint(1, 9)


def color_heading(function):
    def wrapper(*args, **kwargs):
        colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange', 'Pink', 'Black', 'Brown']
        random_color = random.choice(colors)
        return f"<h1 style='color:{random_color}'>" + function(*args, **kwargs) + "</h1>"
    return wrapper


@app.route("/<int:number>")
@color_heading
def user_number(number):
    if number == random_number:
        return 'The number was right!!<br>'\
                '<img src = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzY0YzhwZ201ZnYxcHI3NGttdXY0emtzb3A5M3lwenJiNXN5aTFibCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l1J9wXoC8W4JFmREY/giphy.webp" width=300px>'
    elif number > random_number:
        return 'The number is too high!<br>' \
               '<img src = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbW9pOWs3MnJ0bXlkcGsyOWN5NXRxaDJwYm5rbmh6aHV3MHNkN3dkaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3og0IuWMpDm2PdTL8s/giphy.webp" width=300px>'
    elif number < random_number:
        return 'The number is too low!<br>' \
               '<img src = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXhtNmplaHhtbXNnbGU4dG9xMWQ1cDF0YzFhYWhtdWY0bHp2NzFiMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TgmiJ4AZ3HSiIqpOj6/giphy.webp" width=300px>'

if __name__ == "__main__":
    app.run(debug=True)
