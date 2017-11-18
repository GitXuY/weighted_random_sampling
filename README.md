# weighted_random_sampling
Pure python implementation of weighted random sampling



## Usage

Specify the sample size, items and their cooresponding weights in the code:

    size = <specify size here> 
    weights = {'item1':weights1, 'item2':weights2, ..., 'itemN':weightsN}

Weights can be intergers and float numbers.



## Example

Generate 10000 samples with 10/3 chance to get a red ball, 8/3 chance to get a blue ball, 2/3 chance to get a yellow ball:

    size = 10000
    weights = {'Red':10/3., 'Blue':8/3., 'Yellow':2/3.} 

You can get the following result:

```
Sample size: 10000
Item and weights: {'Blue': 2.6666666666666665, 'Yellow': 0.6666666666666666, 'Red': 3.3333333333333335}
Result: {'Blue': 3986, 'Red': 4962, 'Yellow': 1052}
```

