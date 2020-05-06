import argparse

if __name__ == '__main__':

    average = argparse.ArgumentParser() 

    average.add_argument('--lst', type = int, nargs ='+') 
    average.add_argument('sum', action ='store_const', const = sum) 
    average.add_argument('len', action ='store_const', const = len) 
  
    args = average.parse_args() 

    total = args.sum(args.lst) 

    strleng = args.len(args.lst) 

    listavg = total / strleng 

    print(listavg) 