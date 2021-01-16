from datetime import datetime

VERSION_STRING = '1.0'
RELEASE = False

now = datetime.now()
ver = VERSION_STRING + '_build' + now.strftime('%Y%m%d%H%M%S')
if RELEASE:
  ver += "_release"
else:
  ver += "_dev"
skip_exts = [".py", ".template", ".zip", ".bat", ".merge.json", ".bbmodel", ".ignore", ".ignore.json"]

with open("./resources/pack.mcmeta.template", "r") as fp:
  meta = fp.read()

meta = meta.replace("^VERSION^", ver)

with open("./resources/pack.mcmeta", "w") as fp:
  fp.write(meta)

def check_ext(fn):
  for x in skip_exts:
    if fn.endswith(x):
      return False
  return True

import os
import zipfile
def zipdir(path, ziph):
  # ziph is zipfile handle
  for root, dirs, files in os.walk(path):
    for file in files:
      if not check_ext(file) :
        continue
      full_path = os.path.join(root, file)
      print("Compressing: %s" % full_path)
      ziph.write(full_path, os.path.join(root[11:], file))

zipf = zipfile.ZipFile('ResPackTemplate-%s.zip' % ver, 'w', zipfile.ZIP_DEFLATED)
zipdir('./resources', zipf)
zipf.close()

os.unlink("./resources/pack.mcmeta")
