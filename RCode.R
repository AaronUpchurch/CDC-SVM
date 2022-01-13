# Load Data into dataframe
source("http://www.openintro.org/stat/data/cdc.R")

# Randomize rows
set.seed(41)
rows <- sample(nrow(cdc))
cdc <- cdc[rows,]

# Split into training and test data
training <- cdc[seq(0,.8*nrow(cdc)),]
test <- cdc[seq(.8*nrow(cdc)+1,nrow(cdc)),]

# Check number of rows
print(nrow(training))
print(nrow(test))

# Write data to csv
write.csv(training,"trainning.csv")
write.csv(test,"test.csv")