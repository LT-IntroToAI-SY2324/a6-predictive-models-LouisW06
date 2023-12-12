# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?

My R squared values is 0.86. That means that the model is about 86% accurate in predicting the correct answer based on my data.

2. Is your model accurate? Why or why not?

The model is somewhat accurate, as 0.86 is pretty close to 1, but it is not 100% accurate and still makes mistakes.

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?

The model predicts a 10 year old car to be worth 8988 dollars while the 20 year old car is only 1984 dollars.

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?

I think that the model is using its line of best fit to predict the price without taking into account the fact that cars can't sell for a negative amount of money. We would have to implement a cap at 0 to stop this from happening.