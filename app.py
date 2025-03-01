from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List of Tamil movies with ratings (sorted by rating)
tamil_movies = [
    {"title": "Ponniyin Selvan: Part 1", "rating": 9.3},
    {"title": "Vikram", "rating": 9.2},
    {"title": "Master", "rating": 9.0},
    {"title": "Asuran", "rating": 8.9},
    {"title": "Kaithi", "rating": 8.8},
    {"title": "Soorarai Pottru", "rating": 8.7},
    {"title": "Jai Bhim", "rating": 8.6},
    {"title": "Karnan", "rating": 8.5},
    {"title": "Vada Chennai", "rating": 8.4},
    {"title": "Viswasam", "rating": 8.3},
    {"title": "Bigil", "rating": 8.2},
    {"title": "Sarkar", "rating": 8.1},
    {"title": "Theri", "rating": 8.0},
    {"title": "Mersal", "rating": 7.9},
    {"title": "Darbar", "rating": 7.8},
]

# Initialize the current movie index
current_movie_index = 0

@app.route("/", methods=["GET", "POST"])
def index():
    global current_movie_index

    if request.method == "POST":
        # Increment the index for "Next" button click
        current_movie_index = (current_movie_index + 1) % len(tamil_movies)

    # Fetch the current movie based on the index
    current_movie = tamil_movies[current_movie_index]
    return render_template("index.html", movie=current_movie)

if __name__ == "__main__":
    app.run(debug=True)