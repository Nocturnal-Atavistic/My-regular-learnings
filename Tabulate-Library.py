
from tabulate import tabulate

data = [
    ["Name", "age", "City"],
    ["him", 27, "dubai"],
    ["kim", 34, "san francisco"],
    ["bim", 28, "Bangalore"],

]

x = tabulate(data,
         headers= "firstrow",
         colalign=("left", "right", "Center"),
         showindex= True,
         tablefmt= "grid"
         
         
         )

print(x)    
