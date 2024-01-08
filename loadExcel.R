# Install and load necessary packages
install.packages(c("tidyverse"))
library(tidyverse)
library(dplyr)
library(ggplot2)
library(readxl)

setwd("/Users/crusader/Desktop/courseworkR")
# Load the Excel spreadsheet and list all sheets
excel_file <- file.path(getwd(), "cw.xlsx")  # replace with the actual path to your Excel file

# Use readxl to get sheet names
sheet_names <- excel_sheets(excel_file)

# Print the sheet names
print(sheet_names)

# Part 2 Q 1 ) 
# Import data from Table 3d
table_3_data <- read_excel(excel_file, sheet = "Table 3d")
#print(table_3_data)

# Import data from Table 5
table_5_data <- read_excel(excel_file, sheet = "Table 5")
#print(table_5)

# Import data from Table 7
table_7_data <- read_excel(excel_file, sheet = "Table 7")
#print(table_7)

# Import data from Table 8
table_8_data <- read_excel(excel_file, sheet = "Table 8")
#print(table_8)

#Clean Data 
# Remove rows with NA values from Table 3
cleaned_table3_data <- table_3_data %>%
  filter(complete.cases(.))


# Creating a data frame for banking and credit industry fraud
banking_fraud_df <- cleaned_table3_data %>%
  filter(`Table 3d: Fraud and computer misuse offences referred to the National Fraud Intelligence Bureau (NFIB), with percentage change [note 1, 2, 23, 25]` == "Banking and credit industry fraud") %>%
  select(-1, -ncol(.)) #Remove Last and First Column (Not Needed)

head(banking_fraud_df)
str(banking_fraud_df)


# Creating a data frame for consumer and retail fraud
consumer_fraud_df <- cleaned_table3_data %>%
  filter(`Table 3d: Fraud and computer misuse offences referred to the National Fraud Intelligence Bureau (NFIB), with percentage change [note 1, 2, 23, 25]` == "Consumer and retail fraud [note 14]") %>%
  select(-1, -ncol(.)) #Remove Last and First Column (Not Needed)
head(consumer_fraud_df)
str(consumer_fraud_df)

#Transposing the Row to Column To Plot Boxplot
banking_fraud_df <- as.data.frame(t(banking_fraud_df)) 
consumer_fraud_df <- as.data.frame(t(consumer_fraud_df))


boxplot(as.integer(banking_fraud_df$V1), main = "Dispersion and Central Tendency - Banking Fraud", ylab = "Fraud Committed")
summary(as.integer(banking_fraud_df$V1))

boxplot(as.integer(consumer_fraud_df$V1), main = "Dispersion and Central Tendency - Consumer Retail Fraud", ylab = "Fraud Commited ")
summary(as.integer(consumer_fraud_df$V1))
 
cleaned_table5_data <- table_5_data %>%
  drop_na() %>%
  select(-1, -ncol(.)) %>%
  setNames(.[1, ]) %>%
  slice(-1) %>%
  mutate(
    `Rate per 1,000 population` = as.integer(`Rate per 1,000 population`),
    `Number of offences` = as.integer(gsub(",", "", `Number of offences`))
  )%>%
  filter(`Area Name` != "ENGLAND AND WALES [note 13]") %>%
  filter(`Area Name` != "ENGLAND")

# Get the order of indices for sorting
order_indices_total_offence <- order(cleaned_table5_data$`Number of offences`, decreasing = TRUE)
order_indices_per_offence <- order(cleaned_table5_data$`Rate per 1,000 population`, decreasing = TRUE)

# Sort the data using the order indices
sorted_total_count_desc <- cleaned_table5_data[order_indices_total_offence, ]
sorted_per_count_desc <- cleaned_table5_data[order_indices_per_offence, ]

# Convert 'Area Name' to a factor and order it
sorted_total_count_desc$`Area Name` <- factor(sorted_total_count_desc$`Area Name`, levels = unique(sorted_total_count_desc$`Area Name`))
sorted_per_count_desc$`Area Name` <- factor(sorted_per_count_desc$`Area Name`, levels = unique(sorted_per_count_desc$`Area Name`))

# Aggregate data based on "Area Name" for total count of offences
aggregated_total_count_desc <- sorted_total_count_desc %>%
  group_by(`Area Name`) %>%
  summarize(
    `Number of offences` = sum(`Number of offences`),
    `Rate per 1,000 population` = mean(`Rate per 1,000 population`)
  )

# Convert 'Area Name' to a factor and order it
aggregated_total_count_desc$`Area Name` <- factor(aggregated_total_count_desc$`Area Name`, levels = unique(aggregated_total_count_desc$`Area Name`))

# Plot total count of offences using ggplot2
ggplot(aggregated_total_count_desc, aes(x = `Area Name`, y = `Number of offences`)) +
  geom_bar(stat = "identity", fill = "orange", color = "black") +
  labs(title = " Total Count of Offenses by Region", x = "Region", y = "Number of Offenses") +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1))

# Aggregate data based on "Area Name" for Per 1000 population
aggregated_per_count_desc <- sorted_per_count_desc %>%
  group_by(`Area Name`) %>%
  summarize(
    `Number of offences` = sum(`Number of offences`),
    `Rate per 1,000 population` = mean(`Rate per 1,000 population`)
  )

# Convert 'Area Name' to a factor and order it
aggregated_per_count_desc$`Area Name` <- factor(aggregated_per_count_desc$`Area Name`, levels = unique(aggregated_per_count_desc$`Area Name`))

# Plot Rate per 1,000 population using ggplot2
ggplot(aggregated_per_count_desc, aes(x = `Area Name`, y = `Rate per 1,000 population`)) +
  geom_bar(stat = "identity", fill = "orange", color = "black") +
  labs(title = "Rate per 1,000 population by Region", x = "Region", y = "Rate per 1,000 population") +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1))
