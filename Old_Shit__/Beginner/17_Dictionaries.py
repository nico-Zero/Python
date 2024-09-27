monthConversions = {
    "Jan": "January",
    69: "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}


print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv", "Not a valid key"))
print(monthConversions[69])
