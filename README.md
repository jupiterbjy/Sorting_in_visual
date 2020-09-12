# Sorting in visual

Trying to replicate some sorting actions visually, motived by 'Sounds of Sorting'.

---

#### Old
![Imgur](https://i.imgur.com/EueOoRg.png)

Meh!

---

#### New
Sorts implemented so far:

![Bubble_opt x2](demo/Bubble.webp)
![Cocktail-Shaker_op1 x2](demo/Shaker.webp)
![Selection x2](demo/Selection.webp)
![Insertion x2](demo/Insertion.webp)
![Odd-Even x2](demo/OddEven.webp)
![Heap x3](demo/Heap.webp)
![Merge x2](demo/Merge.webp)
![Quick x2](demo/Quick.webp)
![Counting And Radix_10 x2](demo/Count_Radix.webp)

All those videos are accelerated, factor shown on image description.

Console output speed is too slow to capture sorting under 10 seconds.

And pure Bubble, pure Cocktail-Shaker, Radix base 2 and 4 using bit shift is also implemented, probably not much use tho.

For visualization methods, horizontal_dot is extremely slow as it creates longest lines to overwrite. Bar or Dot is recommended for large N.

---

### How to:

When you run ```async_main.py```, you'll be prompted to type in N of times to sort, Sorting algorithms and visualizing method.

You can input multiple items, but Sorting algorithm section should have to be longest, as other factors are cycled with ```itertools.cycle```.

Example setup that was used for video I've created and split to above images:
```
1 3 13 6 8 5 7 9 4 10 11
20 20 20 20 20 40 40 40 30 40 40
0 1 0 0 0 0 0 0 2 0 0
```
Copy-Paste this and it should show same results, same order.
