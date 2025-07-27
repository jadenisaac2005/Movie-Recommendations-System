# 🎬 Movie Recommendation System

A content-based movie recommendation engine that suggests similar movies based on genre. This project demonstrates an end-to-end machine learning workflow, from data processing and model building to creating an interactive web application with Streamlit.

![App Screenshot](https://i.postimg.cc/43tmSJ5G/Screenshot-2025-07-27-at-11-17-02-PM.png)

---

## ✨ Features

- **Real-time Recommendations**: Instantly get a list of 5 similar movies.
- **Content-Based Filtering**: The recommendation logic is powered by genre similarity using TF-IDF and Cosine Similarity.
- **Interactive UI**: A clean and user-friendly interface built with Streamlit.

---

## 🛠️ Tech Stack

- **Python**: The core programming language.
- **Pandas**: For loading and managing the dataset.
- **Scikit-learn**: For building the recommendation model (TF-IDF Vectorizer, Cosine Similarity).
- **Streamlit**: To create and serve the interactive web application.

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

---

## 🖥️ Usage

Once the setup is complete, you can launch the Streamlit web application with a single command.

```bash
streamlit run app.py
```

---

## 💡 Future Improvements

This project provides a solid foundation. Here are some ways it could be enhanced:

- **Implement Collaborative Filtering**: Use the ratings.csv file to build a model that recommends movies based on the tastes of similar users.
- **Build a Hybrid Recommender**: Combine the current content-based model with a collaborative filtering model for more accurate and diverse recommendations.
- **Add More Content Features**: Enhance the content-based model by including movie cast, director, and keywords in the similarity calculation.
- **Deploy to the Cloud**: Deploy the Streamlit app to a service like Streamlit Community Cloud or Heroku to make it publicly accessible.

---

## 📬 Contact

Jaden Isaac – A B.Tech AI & ML student passionate about building useful projects and exploring the world of technology.

Feel free to reach out with any questions or feedback!

- **GitHub**: [github.com/jadenisaac2005](https://github.com/jadenisaac2005)
- **LinkedIn**: [linkedin.com/in/jaden-isaac](https://linkedin.com/in/jaden-isaac)
