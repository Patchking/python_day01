
import copy

def empty(pures: dict) -> dict:
    return {"gold_ingots": 0}

def add_ingot(purse: dict) -> dict:
    purse_out = copy.deepcopy(purse)
    if "gold_ingots" in purse_out:
        purse_out["gold_ingots"] += 1
    else:
        purse_out["gold_ingots"] = 1
    return purse_out

def get_ingot(purse: dict) -> dict:
    purse_out = copy.deepcopy(purse)
    if "gold_ingots" in purse_out:
        if purse_out["gold_ingots"] > 0:
            purse_out["gold_ingots"] -= 1
        else:
            purse_out["gold_ingots"] = 0
    else:
        purse_out["gold_ingots"] = 0
    return purse_out


def main():
    print("first test: result for 0 - 1 + 1 - 1 + 1 should equal 1")
    first_test = add_ingot(get_ingot(add_ingot(get_ingot(empty({})))))
    print(first_test)
    print()


    print("second test: result should be equal 1 ingot")
    second_test = {"emeralds" : 10, "Apples" : 11}
    print(add_ingot(get_ingot(get_ingot(second_test))))
    print()




if __name__ == "__main__":
    main()