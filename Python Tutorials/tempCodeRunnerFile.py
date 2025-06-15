def seq(a,db):
  db = {
  "seq001": "ATGCGGAATT",
  "seq002": "CGTACGTAGC",
  "seq003": "TTATGCATTA",
  "seq004": "GGAATCCGTA",
  "seq005": "CATGCCGTAGC",
  "seq006": "GGGCGTGCAT",
  "seq007": "AATGCTAGCTA",
  "seq008": "CGCGATGCGC",
  "seq009": "TATATATATA",
  "seq010": "ATGCGGATGCA"
  }
  list=[]
  for key,values in db.items():
     if a == values:
            print(f"Exact match found in: {key}")
seq("ATGC")