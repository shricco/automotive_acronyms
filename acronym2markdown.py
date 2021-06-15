import sys
import re

def convert():
    string_temp="##{}  \n**{}**  \nLatex-Reference: _{}_  \nComment: {}  \n\n"
    with open("automotive_acronyms.tex") as input:
        with open("acronyms.md","w",encoding="utf-8") as output:
            output.write("#Acronyms\n\n")
            for line in input:
                expression=re.compile(r'^\\acro\{(?P<reference>[A-Za-z0-9]+)\}(|\[(?P<acro>[A-Za-z0-9]+)\])\{(?P<long>.*)\}(|.+\%(?P<comment>.*))$')
                result = expression.search(line)
                if result:
                    acro = result.group("acro")
                    reference = result.group("reference")
                    long = result.group("long")
                    comment = result.group("comment")
                    if acro is None:
                        acro=reference
                    output.write(string_temp.format(acro, long, reference, comment))

if __name__ == "__main__":
    convert()
