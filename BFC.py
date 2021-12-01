code = open("code.bf").read();
output=open("bootstrap.c").read();

for c in code: 
    if   c == '>':
        output+="++ptr;"
    elif c == '<':
        output+="--ptr;"
    elif c == '+':
        output+="++*ptr;"
    elif c == '-':
        output+="--*ptr;"
    elif c == '.':
        output+="putchar(*ptr);"
    elif c == ',':
        output+="*ptr = getchar();"
    elif c == '[':
        output+="while (*ptr) {"
    elif c == ']':
        output+="}"

output+="}"

print(output)