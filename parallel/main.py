import multiprocessing as mp

def my_funct(x):
    return x * x





if __name__ == '__main__':
    N = 10
    print(f"Num core cpu : {mp.cpu_count()}")
    with mp.Pool() as pool:
        results = pool.map(my_funct, range(N))

    # Logging the results
    print("Results:")
    for result in results:
        print(result)
