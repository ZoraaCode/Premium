from dump import Dumping

try: Dumping()
except (AttributeError) as e:
  exit(e)
