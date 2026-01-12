text = input("Text:")
a = len(text.replace(" ",""))     #for excluding spaces
print(f"text count(excluding space):", +a)
b = len(text)                    #including spaces
print(f"text cound(including space):", +b)