# Notes

## Data Science

### Precision/Recall/F1 score

Definition of Precision/Recall/F1 Score

### Bias Variance Tradeoff
Variance: Overfitting
Bias: Underfitting

### Hypothesis testing
1. Given an event and a "assumed" probability: An instagram story has 1/2 chance of getting a like
2. H_null: p = 0.5
3. H_alternate: p<0.5
4. You get 10 likes on 100 posts
5. Alternate is correct

### Algorithms

Supervised
1. Linear Regression: House prices
2. Logistic Regression: Binary classification
3. Decision Trees and Random Forests: Credit Scoring Loan Approval
4. Support vector machine: Find the best fit hyperplane

Unsupervised
1. K-means clustering

Reinforcement Learning: Trial and Error approach by reward and penalty

Deep Learning: CNN and RNN, convolution and recurrent

## Python
From Leetcode:
1. New floor division operator: //
2. Gregorian calender problem
3. List comprehension from multiple elements

From Google Colab:
1. Filling empty values in the data table: "df[x].fillna(df[x].mean(), inplace=True)"
2. Combining tables: "df_new[df_x, df_y, on="column_name", how="inner"]"
3. Aljebraic operations: "df_[z] = df[x] +-*/ df[y]"
4. One Hot Encoding: Call getdummies method on the pandas object with the dataframe, column as the arguments

## Remote Sensing
Books referred: https://natural-resources.canada.ca/sites/nrcan/files/earthsciences/pdf/resource/tutor/fundam/pdf/fundamentals_e.pdf
LLM's: Chatgpt
1. Remote sensing is linear transformation from 2 dimension to a 3 dimension space. The loss of the depth dimesion is the null space.
3. Higher-frequency electromagnetic radiation reveals quantum and relativistic behavior more strongly. It's not a question of what lies on the either side of the electromagnetic spectrum.
4. Radiometric resolution measures the energy captured by the pixel on a greyscale.
5. An electromagnetic sensor captures multiple photons and hence the energy varies. The wavelength of the photon may vary, and hence we require 2 separate metric in remote sensing.
6. Related to the spatial resolution: ground area is proportional to denominator, higher the denominator of the scale (1:100) more is the area on the land.
7. Temporal resolution is the revisit time of the satellite.
8. Along the track and Across the track scanners
9. Terms of scanning sensore: ifov, ground resolution, rotating mirror, angular field of view, swath, detector.
10. Primary distortion: relief displacement for objects further away from the nadir.
11. Polarization types: Horizontal, Verticial.
12. HH, VV, HV, VH: First 2 are like polarized transmit and receive, next 2 are cross polarized.
13. Synthetic Aperture Radar uses the flight path to measure the transmitted and received signals.
14. {Pending}
15. Image analysis: Preprocessing, Image Enhancement, Image Transformation, Image Classification and Analysis
16. Preprocessing: Radiometric and Geometric corrections.
17. Image Enhancement: Constrast stretching, spatial filtering, linear contrast stretch of histogram, histogram equalization, image filtering
18. Image Transformation: Combining data from other bands, aljebraic operations etc. Image subtraction, Principle component analysis
19. Image Classification and Analysis: Unsupervised and Supervised
20. 
