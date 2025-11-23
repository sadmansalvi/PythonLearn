import converters     #as converters.py is already in Module_file (everything on converters.py)
from converters import kg_to_lbs    #specific thing from converters.py


print(converters.kg_to_lbs(70))

print(kg_to_lbs(50)) #becuase we specifically imported kg_to_lbs from converters.py




