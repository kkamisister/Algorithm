input_str = input().strip()
croatian_alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for ca in croatian_alphabets:
    input_str = input_str.replace(ca, "*")
print(len(input_str))
