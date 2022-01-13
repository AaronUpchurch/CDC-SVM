# CDC-SVM
Support vector machine created for classifying the health status of respondents to a CDC telephone interview. \n

Respondents were grouped based on their reported general health status \n
  ["Excellent", "Very good", "good"] = 1 \n
  ["Fair","poor"] = 0 \n

Features: \n
  exerany: If respondents exercised in the last month \n
  hlthplan: If respondents had a health plan \n
  smoke100: If respondents smoked 100 or more cigarrettes in their life \n
  height: height in inches \n
  weight: wieght in pounds \n
  wtdesire: Desired weight in pounds \n
  age: Age in years \n
  gender: Gender (m/f) \n
  
  Model accuracy on trianing data: 86.08% \n
  Model accuraccy on test data: 86.63% \n
