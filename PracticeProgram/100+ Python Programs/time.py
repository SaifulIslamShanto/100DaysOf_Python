from datetime import datetime

now = datetime.now()
print(f"{now:%d-%m-%y %H:%m:%S}")