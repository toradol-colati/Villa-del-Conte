import json

with open("translations.js", "r") as f:
    text = f.read()

# removing first line "const translations = {"
# and last line "}; window.translations = translations;"
import re

match = re.search(r'const translations = (\{.*\});\s*window\.translations = translations;', text, flags=re.DOTALL)
if match:
    json_str = match.group(1)
    
    # JavaScript object keys might not be quoted if we were dealing with pure JS, but looking at translations.js, they are unquoted on the top level! 
    # it: {
    # en: {
    # So it won't parse natively as JSON.
    # But let's check basic structure by replacing 'it:', 'en:', etc with '"it":'
    
    json_str = re.sub(r'\b([a-z]{2}):', r'"\1":', json_str)
    
    try:
        json.loads(json_str)
        print("Valid structure")
    except Exception as e:
        print("JSON Error:", e)
else:
    print("Could not match structure")
