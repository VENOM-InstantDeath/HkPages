# AUTHOR: Darth Venom
# CREATED: 02/06/2021
#
# ABOUT: Muestra el tiempo restante del día.
#
# DEPENDS ON: ---

from datetime import datetime

n = datetime.now()
h, m = (n.hour, n.minute)

s=(24*3600)-((h*3600)+(m*60))

print("In hours: %s:%s" % (s//3600, (s%3600)//60))
print("In seconds: %s" % s)
