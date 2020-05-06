import argparse

if __name__ == '__main__':

    multiple = argparse.ArgumentParser()

    multiple.add_argument ('--lst', type = int)

    args = multiple.parse_args()

    result = []
    tmp = None
    for num in args[1:]:
        if num == "-lst":
            if num != None:
                result.append(num)
                tmp = []
        else:
            tmp.append(int(num)**2)
    result.append(num)
    print(result)