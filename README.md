# cmse802project-bc

## Wildfire Risk Prediction and Simulation

This repository contains my final project for CMSE 802: Methods in Computational Modeling at Michigan State University.

The project focuses on analyzing and modeling wildfire risk using a large dataset of historical fire incidents across the United States. It includes steps for data cleaning, exploratory data analysis (EDA), building a basic classification model to identify high-risk fires, and simulating wildfire spread on a grid.

---

## Project Features

- Load and clean historical wildfire data (~1.88 million records)
- Perform exploratory data analysis to identify trends in size, causes, and location
- Train a Random Forest classifier to predict high-risk fires
- Implement a simple 2D simulation that models fire spread over time
- Command-line interface for running key modules like cleaning, modeling, and simulation
- Visualizations to support insights and communicate results

---

## Tools and Libraries

- Python
- pandas, numpy, matplotlib, seaborn
- scikit-learn for modeling
- argparse for CLI support
- Jupyter Notebook for analysis and reporting

---

## Dataset

The dataset used is the [1.88 Million US Wildfires](https://www.kaggle.com/datasets/rtatman/188-million-us-wildfires) dataset from Kaggle. It contains wildfire records from 1992 to 2015 and includes features such as fire size, location, cause, and date of discovery.

---

## Course Information

- **Course:** CMSE 802 – Methods in Computational Modeling  
- **Semester:** Spring 2025  
- **Student:** Bhavya Chawla  
- **University:** Michigan State University

---

## Notes

This project was built with reproducibility and modularity in mind. Scripts can be reused or extended for additional modeling and simulation tasks. The simulation component is a simplified prototype intended for demonstration purposes.

