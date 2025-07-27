# 🎬 Movie Recommendation System

A content-based movie recommendation engine that suggests similar movies based on genre. This project demonstrates an end-to-end machine learning workflow, from data processing and model building to creating an interactive web application with Streamlit.

![App Screenshot](https://i.postimg.cc/43tmSJ5G/Screenshot-2025-07-27-at-11-17-02-PM.png)

---

## ✨ Features

- **Real-time Recommendations**: Instantly get a list of 5 similar movies.
- **Content-Based Filtering**: The recommendation logic is powered by genre similarity using TF-IDF and Cosine Similarity.
- **Interactive UI**: A clean and user-friendly interface built with Streamlit.
- **Dynamic Movie Posters**: Fetches and displays movie posters from the TMDB API to create a visually engaging experience.

---

## 🛠️ Tech Stack

- **Python**: The core programming language.
- **Pandas**: For loading and managing the dataset.
- **Scikit-learn**: For building the recommendation model (TF-IDF Vectorizer, Cosine Similarity).
- **Streamlit**: To create and serve the interactive web application.
- **Requests**: For making API calls to The Movie Database (TMDB).

---

## 📂 Project Structure

The project is contained within a single application script, making it straightforward to understand and run.
```
Movie-Recommendation-System/
│
├── data/
│   └── movies.csv          # The MovieLens dataset
│
├── app.py                  # The complete Streamlit web application script
├── requirements.txt        # Python dependencies
├── README.md               # You are here!
└── LICENSE
```
---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have Python 3.8+ installed on your system.

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Movie-Recommendation-System.git](https://github.com/YOUR_USERNAME/Movie-Recommendation-System.git)
    cd Movie-Recommendation-System
    ```

2.  **Install the required Python libraries:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Download the Dataset:**
    - Download the **MovieLens Small dataset** from [this link](https://files.grouplens.org/datasets/movielens/ml-latest-small.zip).
    - Unzip the file.
    - Create a `data` folder in your project directory.
    - Place the `movies.csv` file inside the `data` folder.

4.  **Add TMDB API Key:**
    - Get a free API key from [The Movie Database (TMDB)](https://www.themoviedb.org/documentation/api).
    - Open the `app.py` file and find the `fetch_poster` function.
    - Replace the placeholder `"YOUR_API_KEY"` with your actual key.

---

## 🖥️ Usage

Once the setup is complete, you can launch the Streamlit web application with a single command.

```bash
streamlit run app.py
```
