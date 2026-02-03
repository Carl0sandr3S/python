
def merge_the_tools(string, k):
    string =   list(map(lambda x: x, string))
    total_string = [string[i:i + k] for i in range(0, len(string), k)]
    
    for i in   total_string:
        print("".join(list(dict.fromkeys(i))))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)