# Content-Based Movie Recommendation System

A simple movie recommendation system built using **Python** and **Streamlit**. The application recommends movies similar to the selected movie using **TF-IDF Vectorization** and **Cosine Similarity**.

---

## Features

- Search for a movie by entering its name.
- Recommends the top 5 similar movies.
- Interactive web interface built with Streamlit.
- Uses a content-based recommendation approach.

---

## Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Pickle

---

## How It Works

1. Movie data is loaded and preprocessed.
2. TF-IDF Vectorization converts movie overviews into numerical feature vectors.
3. Cosine Similarity measures the similarity between movies.
4. The similarity matrix is saved as a Pickle file.
5. The Streamlit application recommends the five most similar movies based on the selected title.

---

## Project Structure

```
content-based-movie-recommendation-system/
│
├── app.py
├── notebooks/
│   └── movie_recommendation.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

```bash
git clone https://github.com/sakshiSE/content-based-movie-recommendation-system.git

cd content-based-movie-recommendation-system

pip install -r requirements.txt
```

## Running the Project

## Dataset

This project uses the **TMDB 5000 Movie Dataset**, which contains movie metadata and credits.

**Download the dataset from Kaggle:**

:contentReference[oaicite:0]{index=0}

After downloading, place the dataset files in the `data/` folder:

```
data/
├── tmdb_5000_movies.csv
└── tmdb_5000_credits.csv
```

1. Open the notebook in the `notebooks` folder.
2. Run all cells to preprocess the dataset and generate the required model files.
3. After the model files are generated, start the Streamlit application.

```bash
streamlit run app.py

```

## Note

The generated `.pkl` files are not included in this repository. Running the notebook creates the required files automatically.

---

## Example

**Input**

```
Interstellar
```

**Output**

```
The Martian
Gravity
Moon
Contact
Sunshine
```
