import mimesis
from mimesis.locales import Locale

text = mimesis.Text(Locale.EN)

print(text.text(quantity=20))
