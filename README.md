# Spotify Song Recommendations Project

## Overview
This project, titled "Project #14," was created by Shlok Sheth. The primary goal of this project is to implement recommendation systems. The code is designed to provide show recommendations based on user preferences and interactions with different shows.

## Project Files
All the data file are situated in the repository.

## Data Source
The code utilizes a dataset stored in a CSV file named 'show_rec_data.csv.' The data is loaded into a Pandas DataFrame for analysis and recommendations.

## Code Description
The code defines several functions for calculating similarities between shows and users, ultimately providing show recommendations. Key functions include:
- `dot_product`: Calculates the dot product of two vectors.
- `vector_norm`: Calculates the norm of a vector.
- `cosine_similarity`: Computes the cosine similarity between two vectors.
- `get_show_recommendations`: Provides show recommendations based on user preferences.
- `get_similar_artists`: Identifies users with similar preferences for a given user.
- `get_user_recommendations`: Recommends shows for a given user based on the preferences of similar users.

## Example Usage
The code demonstrates how to obtain show recommendations based on users who watch specific shows and suggests new shows for users who have not seen certain content.

```python
# Show recommendation based on users who watch show_1
print(f"Show recommendation based on users who watch show_1 {get_show_recommendations(data_t,'show_1')[0:4]}.")

# Show recommendation based on users who watch show_5
print(f"Show recommendation based on users who watch show_5 {get_show_recommendations(data_t,'show_5')[0:4]}.")

# New show recommendation for user 2
print(f"New show recommendation for user 2 {get_user_recommendations(data_t,2)[0:4]}.")

# New show recommendation for user 100
print(f"New show recommendation for user 100 {get_user_recommendations(data_t,100)[0:4]}.")
```

## Interpretation of Results
The output of the code provides insights into user preferences and recommendations for streaming businesses. For example, recommendations based on user interactions with specific shows can guide streaming platforms in suggesting content that aligns with user preferences.

## Conclusion
This code serves as a foundation for implementing recommendation systems for shows on streaming platforms, providing valuable insights for content recommendations tailored to user preferences.
