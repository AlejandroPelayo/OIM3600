# Output:

```
# Output goes here
Now sorting random5000.txt:
Selction Sorting running time: 0.46559858322143555s
Bubble Sorting running time: 1.1614196300506592s
Merge Sorting running time: 0.013032913208007812s

Now sorting random10000.txt:
Selction Sorting running time: 1.892486810684204s
Bubble Sorting running time: 4.604727745056152s
Merge Sorting running time: 0.0434417724609375s

Now sorting random50000.txt:
Selction Sorting running time: 46.51884961128235s
Bubble Sorting running time: 107.45610880851746s
Merge Sorting running time: 0.1288444995880127s

Now sorting sorted5000.txt:
Selction Sorting running time: 0.4480102062225342s
Bubble Sorting running time: 0.00021767616271972656s
Merge Sorting running time: 0.0052525997161865234s

Now sorting sorted10000.txt:
Selction Sorting running time: 1.835836410522461s
Bubble Sorting running time: 0.0005686283111572266s
Merge Sorting running time: 0.020557641983032227s

Now sorting sorted50000.txt:
Selction Sorting running time: 41.045628786087036s
Bubble Sorting running time: 0.0055179595947265625s
Merge Sorting running time: 0.06441092491149902s

Now sorting reversed5000.txt:
Selction Sorting running time: 0.4085502624511719s
Bubble Sorting running time: 1.105478048324585s
Merge Sorting running time: 0.004731416702270508s

Now sorting reversed10000.txt:
Selction Sorting running time: 1.6026530265808105s
Bubble Sorting running time: 4.915395498275757s
Merge Sorting running time: 0.011730670928955078s

Now sorting reversed50000.txt:
Selction Sorting running time: 47.947176933288574s
Bubble Sorting running time: 133.2297511100769s
Merge Sorting running time: 0.11249613761901855s

```


# Results Analysis
That took a long time. Selection sort was pretty slow in every test. its very basic and as the data gets bigger selection sort takes increasingly long. This is due to its linear time complexity so it struggled with larger datasets. But it did about the same in random, sorted, and reversed because its about the lengeth of the data not how the data is displayed

Bubble was the slowest overall. It really struggled with reverse and random data sets but unlike selection sort that is the same speed on all, bubble was very fast when the data was sorted.

Merge sort was the fastest by far. It did not matter if it was random, sorted, or reversed, or even how large the data set was. Merge sort, because of its log time complexity, vastly outperformed bubble and selection. This is due to the fact that merge sort "divides and conquores" the data allowing it to be fast even in very large data sets.
