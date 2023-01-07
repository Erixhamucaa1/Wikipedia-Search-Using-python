# Importing Wikipedia module
# To install pip install wikipedia
import wikipedia  as wiki

# Setting language here english is set
wiki.set_lang("om")

# Printing the summary from wikipedia
print(wiki.summary("Python"))