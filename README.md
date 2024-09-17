# FLARE: Federated Learning And Resilient Encryption for Firewalls
> The official research paper can be found at ```To be published```

FLARE is a novel approach to redefine the design of firewalls. Traditional firewalls generally rely on static rule sets, which can be exploited by advanced algorithms. This issue was addressed with the introduction of machine learning-based firewalls, which adapt to dynamic threats by learning patterns and behaviors from network traffic. However, these firewalls face challenges in data privacy and security, as the training data often contains sensitive information. FLARE mitigates this by integrating federated learning and resilient encryption, ensuring that the firewall can learn from distributed data sources without compromising the confidentiality of the data, thus enhancing both security and performance.

## Analysis of Algorothims

### K-Nearest Neighbour 
The K-Nearest Neighbors (KNN) algorithm is a simple, instance-based machine learning algorithm used for classification and regression tasks. It works by finding the "k" nearest data points to a given input based on a distance metric, usually Euclidean distance. In classification, the algorithm assigns the input to the most common class among its nearest neighbors, while in regression, it predicts the value by averaging the values of the k nearest points. KNN is non-parametric and relies on the assumption that similar data points exist near each other in the feature space.

**Accuracy: 0.8653792134831461**

Classification Report:

| Class       | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| accept      | 0.63      | 0.47   | 0.54     | 1622    |
| client-rst  | 0.86      | 0.93   | 0.89     | 27852   |
| close       | 0.89      | 0.84   | 0.86     | 19266   |
| deny        | 0.98      | 0.96   | 0.97     | 1993    |
| server-rst  | 0.82      | 0.69   | 0.75     | 4792    |
| timeout     | 0.84      | 0.88   | 0.86     | 4555    |


### Support Vector Machines 
Support Vector Machines (SVM) is a powerful supervised machine learning algorithm used for both classification and regression tasks, though it is mainly used for classification. The core idea of SVM is to find the optimal hyperplane that best separates the data points of different classes in a high-dimensional space. The data points that are closest to the hyperplane are called support vectors, and they help define the decision boundary.

In cases where the data is not linearly separable, SVM uses a technique called the kernel trick to map data into a higher-dimensional space where a linear separation is possible. Common kernels include linear, polynomial, and radial basis function (RBF). SVM is known for its effectiveness in high-dimensional spaces and is widely used in applications like text classification, image recognition, and bioinformatics.

**Accuracy: 0.5099192415730337**

Classification Report:

| Class       | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| accept      | 0.00      | 0.00   | 0.00     | 1622    |
| client-rst  | 0.50      | 0.99   | 0.67     | 27852   |
| close       | 0.68      | 0.04   | 0.07     | 19266   |
| deny        | 0.96      | 0.36   | 0.53     | 1993    |
| server-rst  | 0.00      | 0.00   | 0.00     | 4972    |
| timeout     | 0.00      | 0.00   | 0.00     | 1255    |


### Logistic Regression
Logistic Regression is a popular supervised machine learning algorithm used for binary classification tasks. Despite its name, it is actually a linear model that predicts the probability of an input belonging to a certain class (usually between 0 and 1). It uses the logistic function (also called the sigmoid function) to model the probability. The output is a value between 0 and 1, which is then converted into a binary label (e.g., 0 or 1) based on a threshold, typically 0.5.

Logistic Regression is widely used in fields such as healthcare, marketing, and finance for predicting outcomes like disease presence, customer churn, or credit default. It is easy to implement, interpretable, and works well when the relationship between the input features and the class labels is approximately linear.

**Accuracy: 0.586060393258427**

Classification Report:

| Class       | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| accept      | 0.52      | 0.14   | 0.22     | 1622    |
| client-rst  | 0.57      | 0.83   | 0.68     | 27852   |
| close       | 0.61      | 0.44   | 0.51     | 19266   |
| deny        | 0.91      | 0.75   | 0.82     | 1993    |
| server-rst  | 0.42      | 0.00   | 0.01     | 4972    |
| timeout     | 0.01      | 0.00   | 0.01     | 1255    |


### Random Forest
Random Forest is an ensemble learning method used for both classification and regression tasks. It works by constructing multiple decision trees during training and combining their outputs to make more accurate and stable predictions. For classification, the random forest algorithm takes a "majority vote" from all the decision trees, while for regression, it averages the predictions of the trees.

The key idea behind Random Forest is randomness—each tree is trained on a random subset of the data, and at each node, the best split is chosen from a random subset of features. This helps in reducing overfitting and improves the model's generalization.

Random Forest is highly accurate, robust to noisy data, and effective for both small and large datasets. It is widely used in various domains like finance, healthcare, and fraud detection.

**Accuracy: 0.9469803370786517**

Classification Report:


| Class | Precision | Recall | F1-score | Support |
|---|---|---|---|---|
| accept | 0.81 | 0.85 | 0.83 | 1622 |
| client-rst | 0.94 | 0.98 | 0.96 | 27852 |
| close | 0.97 | 0.93 | 0.95 | 19266 |
| deny | 1.00 | 1.00 | 1.00 | 1993 |
| server-rst | 0.93 | 0.82 | 0.87 | 4972 |
| timeout | 1.00 | 0.99 | 0.99 | 1255 |



