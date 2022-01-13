# CDC-SVM
Support vector machine created for classifying the health status of respondents to a CDC telephone interview  

Respondents were grouped based on their reported general health status  
  ["Excellent", "Very good", "good"] = 1  
  ["Fair","poor"] = 0  

Features:  
  exerany: If respondents exercised in the last month  
  hlthplan: If respondents had a health plan  
  smoke100: If respondents smoked 100 or more cigarrettes in their life  
  height: height in inches  
  weight: wieght in pounds  
  wtdesire: Desired weight in pounds  
  age: Age in years  
  gender: Gender (m/f)  
  
  Model accuracy on trianing data: 86.08%  
  Model accuraccy on test data: 86.63%  
