a=input("Enter the reference genome :")
b=input("Enter the patient genome   :")
if len(a)==len(b):
  for i in range(len(a)):
    if a[i]!=b[i]:
      print(f"SNP at position {i} :{a[i]}-->{b[i]}")