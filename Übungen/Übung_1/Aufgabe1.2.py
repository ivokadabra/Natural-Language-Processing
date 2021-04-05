import re
s1 = "Herr Josef Meier kann auch als J. oder Joseph oder Jupp oder Sepp bennen.Mayer , Maier und M. sind die andere Altenativen"
p = re.findall(r"[JS][.|ose|u]*[pfh]*|M[ae][iy][ea]?r|M[.]", s1,re.DOTALL)
#print(p.group(1))
for i in p:
    print(i)