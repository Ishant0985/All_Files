def count_substring(string, substring):
    count =0
    sub_len = len(substring)
    for i in range(len(string) - sub_len+1):
        if string[i:i + sub_len] == substring:
            count += 1
        return count
if __name__== "__main__":
    string = input().strip()
    substring = input().strip()
    result = count_substring(string, substring)
    print(result)
    
    



def count_substring(string, substring):
     count =0
     sub_len = len(substring)
     for i in range(len(string) - sub_len+1):
         if string[i:i + sub_len] == substring:
             count += 1
     return count

# if __name__ == "__main__":
#     string = input().strip()
#     substring = input().strip()
#     result = count_substring(string, substring)
#     print(result)