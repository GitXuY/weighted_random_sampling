import random
from collections import Counter


def calculate_normalized_weights(weights):
    normalized_weights = weights.copy()
    
    sum = get_total_weights(weights)

    for item, weight in weights.iteritems():
        normalized_weights[item] = float(weight) / sum

    return normalized_weights


def get_total_weights(weights):
    sum = 0
    for weight in weights.values():
        sum += weight

    return sum


def weighted_random_sample(size, weights, seed=1001):
    normalized_weights = calculate_normalized_weights(weights)
    result = list()
    
    for i in xrange(size):
        random_num = random.random()
        for item, weight in normalized_weights.iteritems():
            random_num -= weight
            if random_num <= 0:
                result.append(item)
                break

    return result


def main():
    size = 10000 #specify size here
    weights = {'Red':10/3., 'Blue':8/3., 'Yellow':2/3.} #specify items and weights here format: 'item':weight

    result = weighted_random_sample(size, weights) 
    print "Sample size:", size
    print "Item and weights:", weights
    print "Result:", dict(Counter(result))

if __name__ == '__main__':
    main()