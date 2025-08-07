#| Feature           | List    | Tuple      | Set           | Array (`array`) | Dictionary                |
#| ----------------- | ------- | ---------- | ------------- | --------------- | ------------------------- |
#| Mutable           | ✅       | ❌          | ✅             | ✅               | ✅                       |
#| Ordered           | ✅       | ✅          | ❌             | ✅               | ✅ (since Python 3.7)    |
#| Allows Duplicates | ✅       | ✅          | ❌             | ✅               | Keys ❌, Values ✅       |
#| Indexable         | ✅       | ✅          | ❌             | ✅               | ❌ (key-access instead)  |
#| Key-Value Pairs   | ❌       | ❌          | ❌             | ❌               | ✅                       |
#| Data Types        | Mixed   | Mixed      | Hashable only | Homogeneous     | Keys hashable, values any |
#| Use Case          | General | Fixed data | Unique items  | Numeric data    | Mapped/structured data    |


list_ = [1,2,3,4,5]

tuple_ = (1,2,3,4,5)

set_ = {1,2,3,4,5}

dict_ = {"1": 1, "2": "2"}

import array
# Create an array of integers
array_ = array.array('i', [1, 2, 3, 4, 5])  # 'i' = integer