import os
import pandas as pd

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")
id_of_item = input("Podaj kod produktu: ")

opinions = pd.read_json("opinions/"+id_of_item+".json")
print(opinions)