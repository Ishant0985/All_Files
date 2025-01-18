# s1 = "Ishant Yadav"
# s2 = "      my name is ishant yadav.   "
# print(s2.swapcase())
# print(s2.startswith("my"))
# print(s2.isalnum())
# print(f"{s2.isalpha()} lets check")
# print(s2.endswith("yadav"))
# print(s1.isprintable(),s2.isprintable())
# print(s2.istitle())
# s3 = s2.capitalize()
# print(s3)
# print(s3.title())
# s4 = s2.swapcase()
# print(s4.isupper())
# print(s4.lower())
# print(s2.strip())
# print(s2.rstrip())
# print(s2.lstrip())
# s5 = s1.split()
# print(s5)
'''Below is very important shortcut to split and 
join string & print them by writting single line'''
# line = "this is a string"
# print("-".join(line.split(" ")))
# def count_substring(string, substring):
#     count =0
#     sub_len = len(substring)
#     for i in range(len(string) - sub_len+1):
#         if string[i:i + sub_len] == substring:
#             count += 1
#     return count

# if __name__ == "__main__":
#     string = input().strip()
#     substring = input().strip()
#     result = count_substring(string, substring)
#     print(result)
    
    
# def count_substring(string, sub_string):
#     count =0
#     sub_len = len(sub_string)
#     for i in range(len(string)-sub_len+1):
#         if string[i:i +sub_len] == sub_string:
#             count += 1
#     return count

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)