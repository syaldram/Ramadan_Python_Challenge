from collections import deque


def tail(log: str, n: int):
    
    last_lines = []
    
    with open(log) as fin:
        last_n_line = deque(fin, maxlen=n)
    
    unclean_lst = list(last_n_line)
    for line in unclean_lst:
        line = line.replace("\n", "")
        last_lines.append(line)

    return last_lines
    
    
    
    




if __name__ == "__main__":
    
    print(tail("./logs/test_log.txt", 3))
    print(tail("./logs/test_log.txt", 1))
    print(tail("./logs/test_log.txt", 0))
    