
import argparse

if __name__ == '__main__':
    
    duplicates = argparse.ArgumentParser()

    duplicates.add_argument ('--lst', type = str)

    args = duplicates.parse_args()

    output = ""

    for word in args[2:]:
    
        result = ""
    
        for x in word:
            
            if x not in result:
                result += x
    
        output += (result+" ")
    
    output = output[:-1]
    print(output)
    