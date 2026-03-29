import pandas as pd
import matplotlib.pyplot as plt



#load dataset
df = pd.read_csv("C:/Users/kamal/PyCharmMiscProject/.venv/helpdesk_tickets.csv")

df.columns = df.columns.str.strip()

print("First 5 rows")
print(df.head())
print("\nColumn names:")
print(df.columns)


#Basic metrics
print("\nTotal Tickets:", len(df))
print("Average Resolution Time:", df["Resolution_Hours"].mean())

#Most common issue categories
issue_counts = df["Issue_Category"].value_counts()
print("\nMost Common Issues Categories:")
print(issue_counts)

#Tickets by department
department_counts = df["Department"].value_counts()
print("\nTicket by Department:")
print(department_counts)

#Average resolution time by issue category
ave_resolution_by_issue = df.groupby("Issue_Category")["Resolution_Hours"].mean().sort_values(ascending=False)
print("\nAverage Resolution Time by Issue Category:")
print(ave_resolution_by_issue)

#Plot issue categories
issue_counts.plot(kind="bar")
plt.title("Help Desk Tickets by Issue Category")
plt.xlabel("Issue Category")
plt.ylabel("Number of Tickets")
plt.tight_layout()
plt.show()
print("\nMost Common Tickets by Department:")

#Plot average resolution time by issue category
ave_resolution_by_issue.plot(kind="bar")
plt.title("Average Resolution Time by Issue Category")
plt.xlabel("Issue Category")
plt.ylabel("Hours")
plt.tight_layout()
plt.show()
