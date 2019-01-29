# cspath-datastructures-capstone-project

1. Which data structure(s) did you use for part 1? Why did you select these data structures?

A Trie structure. I wanted to explore the efficiency involved with searching for words in a Trie.

2. What is the runtime (in asymptotic notation) of searching for a food type? Do you think there is a more efficient runtime?

Worst case scenario: O(N*26) = O(N)
where N is the length of the string
(this is ignoring the data insertion into the trie which is required before searching can take place)

3. Which data structures did you use for part 2? Why did you select these data structures?

Hash Map and Linked List. Hash maps are most efficient for retrieving a value based on a key value pair. I used a Hash Map to retrieve a Linked List of restaurants
based on a restaurant type value. Once the restaurant type is known, a Linked List works find to store the options. Each item in the Linked List was also a Hash Map object.

4. What is the runtime (in asymptotic notation) of retrieving the restaurant data? Do you think there is a more efficient runtime?

O(1) + O(N) + O(1) = O(N)
where N is the number of restaurants returned

It's possible there is a more efficient runtime if different data structures were used or if the data was organized in a different way. Because a Linked List is used
to store the restaurants for each restaurant type, we need to iterate through the list which gives us O(N) runtime.

5. Outside of this project, what are other innovative ways you can utilize data structures?

I plan to implement a queue data structure to enable concurrent processing so that while data is being uploaded to the queue, another process will begin processing
items in the queue.
