params_appliance = {
    'microwave': {
        'windowlength': 599,
        'on_power_threshold': 200,
        'max_on_power': 3969,
        'mean': 500,
        'std': 800,
        's2s_length': 128,
        'houses': [1, 5],
        'channels': [11, 3],
        'train_build': [4, 5, 6],
        'test_build': 1
    },
    'fridge': {
        'windowlength': 599,
        'on_power_threshold': 50,
        'max_on_power': 3323,
        'mean': 200,
        'std': 400,
        's2s_length': 512,
        'houses': [1, 4, 5, 6],
        'channels': [5, 9, 7],
        'train_build': [4, 5, 6],
        'test_build': 1
    },
    'dishwasher': {
        'windowlength': 599,
        'on_power_threshold': 10,
        'max_on_power': 3964,
        'mean': 700,
        'std': 1000,
        's2s_length': 1536,
        'houses': [1, 4, 5, 6],
        'channels': [6, 15, 20, 9],
        'train_build': [4, 5, 6],
        'test_build': 1
    },
    'washingmachine': {
        'windowlength': 599,
        'on_power_threshold': 20,
        'max_on_power': 3999,
        'mean': 400,
        'std': 700,
        's2s_length': 2000,
        'houses': [1, 4, 5, 6],
        'channels': [20, 7, 13],
        'train_build': [4, 5, 6],
        'test_build': 1
    },
    'kitchenoutlet': {
        'windowlength': 599,
        'on_power_threshold': 2,
        'max_on_power': 1737,
        'mean': 12,
        'std': 28,
        's2s_length': 2000,
        'houses': [1, 2, 3, 4, 5, 6],
        'channels': [7, 3, 21, 5, 24, 3],
        'train_build': [1, 2, 3, 4],
        'test_build': [5, 6]
    },
    'stove': {
        'windowlength': 599,
        'on_power_threshold': 1,
        'max_on_power': 2080,
        'mean': 4,
        'std': 51,
        's2s_length': 2000,
        'houses': [1, 2, 4, 6],
        'channels': [14, 5, 8, 5],
        'train_build': [1, 2, 4],
        'test_build': 6
    }
}