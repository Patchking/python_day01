import ex00
import math
import sys

def split_booty(*purges) -> list:
    gold_count = sum([purge["gold_ingots"] for purge in purges if "gold_ingots" in purge])
    out = []
    out.append(math.floor(gold_count / 3))
    out.append(round(gold_count / 3))
    out.append(math.ceil(gold_count / 3))
    return tuple(out)

def main():
    for i in range(0, 100, 7):
        print("total purges count", i, "    ", end="")
        list_of_purges = [ex00.add_ingot({}) for i in range(i)]
        print(split_booty(*list_of_purges))

if __name__ == "__main__":
    main()