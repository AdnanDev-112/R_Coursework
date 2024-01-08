# Example Data
data <- data.frame(
  Year = rep(c("Apr 2012 to Mar 2013", "Apr 2013 to Mar 2014", "Apr 2014 to Mar 2015",
               "Apr 2015 to Mar 2016", "Apr 2016 to Mar 2017", "Apr 2017 to Mar 2018",
               "Apr 2018 to Mar 2019", "Apr 2019 to Mar 2020", "Apr 2020 to Mar 2021",
               "Apr 2021 to Mar 2022 [note 28]"), each = 10),
  Value = c(306641, 286234, 320495, 367714, 380390, 352064, 386326, 433336, 384886, 552024)
)

# Convert "Year" to a factor with ordered levels
data$Year <- factor(data$Year, levels = unique(data$Year), ordered = TRUE)

# Boxplot
boxplot(Value ~ Year, data = data, main = "Box Plot", xlab = "Year", ylab = "Value", col = "skyblue")
