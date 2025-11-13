# <span style="color:#FF4B4B;">Movie Recommendation System</span>

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?style=for-the-badge&logo=github)](https://github.com/Ishika-guptaa25)
[![Stars](https://img.shields.io/github/stars/Ishika-guptaa25/Movie_Recommendation_System?style=for-the-badge&logo=github)](https://github.com/Ishika-guptaa25/Movie_Recommendation_System/stargazers)
[![Forks](https://img.shields.io/github/forks/Ishika-guptaa25/Movie_Recommendation_System?style=for-the-badge&logo=git)](https://github.com/Ishika-guptaa25/Movie_Recommendation_System/network)

> **Discover movies quickly and efficiently with similarity-based recommendations. Fully interactive Streamlit app.**

---

## <span style="color:#3776AB;">Features</span>

- Recommend movies based on user-selected movie  
- Similarity-based recommendations using precomputed `.pkl` models  
- Interactive Streamlit web interface  
- Handles large datasets using Git LFS  
- Fast, real-time recommendations  

---

## <span style="color:#FF4B4B;">Project Structure</span>

<img width="760" height="517" alt="image" src="https://github.com/user-attachments/assets/d5332583-ecb3-450a-b22d-68ddcbbe6fd1" />

---

## <span style="color:#3776AB;">How It Works / Methodology</span>

1. **Data Source:** TMDb dataset with movies, genres, and overviews.  
2. **Feature Engineering:**  
   - Combine genres, cast, keywords, and overview into a single “tags” column.  
3. **Vectorization:** Convert tags into numerical vectors using **CountVectorizer**.  
4. **Similarity Calculation:** Compute **cosine similarity** between movies.  
5. **Recommendation:** Return top 5 most similar movies for the selected input.  
6. **Interface:** Streamlit app allows users to type/select a movie and view recommendations instantly.  

---

## <span style="color:#3776AB;">Demo</span>

<div style="background-color:#f2f2f2; padding:10px; border-radius:8px;">
<img width="1130" height="807" alt="Demo" src="https://github.com/user-attachments/assets/4c114ded-8241-4823-9659-d9764767c729" />
</div>

---

## <span style="color:#FF4B4B;">Try Online</span>

[Run the App Online](https://movierecommendationsystem-ncrtjedukwuqxxkgzx2aic.streamlit.app/)  

No setup required — try it instantly in your browser.

---

## <span style="color:#3776AB;">How to Run Locally</span>


### Clone repository
git clone https://github.com/Ishika-guptaa25/Movie_Recommendation_System.git
cd Movie_Recommendation_System

### Install dependencies
pip install -r requirements.txt

### Download LFS files
git lfs pull

### Run the Streamlit app
streamlit run app.py
<span style="color:#3776AB;">Usage</span>
Type or select a movie name in the input box

Click Recommend

View the recommended movie list instantly

---

## <span style="color:#3776AB;">Dependencies</span>
Python >= 3.8

Streamlit

Pandas

scikit-learn

Pickle

---

# Install all dependencies via:

pip install -r requirements.txt
<span style="color:#3776AB;">Notes</span>
Ensure .pkl files are downloaded using Git LFS

Large files (>25MB) are tracked automatically with Git LFS

Run in a virtual environment to avoid conflicts

Update LFS files if missing with git lfs pull

---

## <span style="color:#3776AB;">Future Improvements</span>
Add collaborative filtering or hybrid recommendation system

Deploy online using Heroku / Streamlit Cloud

Add user profiles and history-based recommendations

Improve UI/UX and add movie ratings

---

## <span style="color:#FF4B4B;">Author</span>
Ishika Gupta

Email: ishikagpt1@gmail.com

GitHub: https://github.com/Ishika-guptaa25

“Analyze what you see, build what you dream.” — Ishika Gupta


---














