from wikiem.feature_correlation import bilingual_sim

test_pairs = [['hello kitty','pokemon'],['Newton','Einstein'],['twitter', 'facebook'], ['bird flu', 'world war']]

def main():
    results = []
    for pair in test_pairs:
        similarity = bilingual_sim(pair[0], pair[1])
        results.append([pair[0], pair[1], similarity])
    print(results)

if __name__ == '__main__':
    main()