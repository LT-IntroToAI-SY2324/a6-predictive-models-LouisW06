# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
Without the standard scaler, my model is extremely inacuate, as the standard scaler makes all the values in between 0 to 1 so the graph doesn't get skewed. 
2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
The model is much more accurate because the values are scaled so the graph isn't so drastic.
3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
The model overall was mostly accurate. There were a few times when it predicted that a buyer purchased something but it actually didn't purchase, which is because the code is merely an estimate based on a graph and not 100% accurate. 
4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.
No, she would not buy an SUV according to the model.
