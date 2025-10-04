# Real Estate Data Analysis (Divar Dataset)

This project is a **data analysis case study** based on the [Divar Real Estate Ads Dataset](https://huggingface.co/datasets/divarofficial/real_estate_ads).
The goal was to explore, clean, and analyze real-estate data to extract meaningful insights about property features such as land size, building size, room count, and construction year.

---

## 📦 Requirements

To run this project, install the required dependencies:

```bash
pip install -r requirements.txt
```

The project uses the following main libraries:

* **datasets** → loading the dataset from Hugging Face
* **pandas** → data wrangling and preprocessing
* **numpy** → numerical operations
* **matplotlib / seaborn** → data visualization
* **scikit-learn** → preprocessing and simple ML utilities
* **scipy** → statistical analysis

---

## 📊 Project Workflow

1. **Dataset Loading**

   * Loaded the dataset `divarofficial/real_estate_ads` from Hugging Face.
   * Converted it into a Pandas DataFrame for further processing.

2. **Data Cleaning**

   * Removed missing or irrelevant values.
   * Focused on important variables:

     * `land_size`
     * `building_size`
     * `rooms_count`
     * `construction_year`

3. **Exploratory Data Analysis (EDA)**

   * Visualized distributions of numerical features.
   * Checked correlations between land size, building size, and room count.
   * Identified outliers and anomalies using statistical methods (e.g., z-score, IQR).

4. **Statistical Insights**

   * Used **Scipy stats** to validate hypotheses.
   * Generated descriptive statistics (mean, median, mode, variance, etc.).

5. **Visualization**

   * Plotted histograms, barplots, and boxplots to showcase feature distributions.
   * Highlighted relationships between construction year and property size.

---

## 📈 Key Findings

* Larger land sizes generally correlate with higher room counts.
* Certain construction years cluster around economic booms in the housing market.
* Outlier detection showed significant noise in building size values, which required cleaning.
* Data distributions confirmed a **right-skewed pattern** for both land and building sizes.

---

## 🚀 How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/<your-username>/portfolio.git
   cd portfolio/Data_Analysis
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the notebook:

   ```bash
   jupyter notebook divar.ipynb
   ```

---

## 📌 Notes

* This project focuses on **EDA (Exploratory Data Analysis)** rather than predictive modeling.
* Due to dataset size, raw data is not included here — it will be downloaded directly from Hugging Face when running the notebook.

---

## 📷 Sample Visualizations

*(Add plots/screenshots from your notebook here to make the README visually appealing.)*
