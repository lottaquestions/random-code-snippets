import bisect

translations = [['eng', "yes"], ['fr',"oui" ], ['swe', "ja"]]
new_lang = ['sw', "ndio"]

# Find the correct spot to insert new_lang into the translations list
index = bisect.bisect([lang for lang, _ in translations], new_lang[0])

# Insert new_lang into the translations list at the correct spot
translations.insert(index, new_lang)

print(translations)
