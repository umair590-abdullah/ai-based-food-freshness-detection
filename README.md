The overall workflow for the project can be represented 
as:
****User Image -> Image Preprocessing -> CNN Model -> 
Freshness Classification -> Confidence Score -> Decision 
Making -> Safety Guidance -> Recipe Recommendation ****

The user first captures or uploads an image of food. The 
image is then preprocessed and passed to the trained CNN 
model. The model predicts the freshness category and 
generates a confidence score. Based on the prediction and 
confidence level, the system provides an appropriate result or 
requests another image when the prediction is uncertain. For 
food that appears visually suitable for use, the system can 
provide recipe recommendations to encourage timely
utilization and reduce food waste. The framework is 
intentionally designed so that recipe recommendation
remains separate from a food-safety guarantee.


