# MaRS Recruitment Task-1

## 🧠 Learning Experience

Each of the questions attacked different aspects allowing me to have to think and work through the code. The light dose featured ubuntu which installing it in itself was a nice learning experience it was nice tampering with my laptop and figuring things out, and learning the linux commands. Coming into the medium dose though I didn't learn much new things, it was nice tackling new questions and thinking through the different approaches for solving things like matrices or decryption or processing data. It allowed me to study into coordinate geometry and the numpy module and collections module further and see how each function worked and operated. It also helped me learn few basics of morse code and how the gaps between the symbols have different meanings. When I entered hard dose it was something completely new. The first question was fairly straightforward though it took me sometime to understand how to solve. The second question was something I had very little idea in and had to do some research to learn about pin-hole cameras and how to calculate the focal length. Though I was unable to completely solve this question it still helped me learn the basic concepts. I also got to learn behavior trees and how they worked and why they are useful. Overall this was a fun and challenging learning curve which helped me strengthen my basics and learn new things.

---

## 📐 Equations, Theorems, and Sketches

### 1. Graph Traversal Theorem (Task 1)
For the rover pathfinding, I used the **Breadth-First Search (BFS)**. The movement cost between grid tiles is uniform so BFS automatically helps to find the shortest path which is particularly useful as that serves as the bonus question

### 2. The Pinhole Camera Model (Task 2)
To calculate the distance of the arrow using a 2D camera feed, I used the principle of Similar Triangles which is useful for pinhole cameras.
First, calculating the focal length from the 55-degree Diagonal Field of View:
$$Focal Length = \frac{Diagonal_{px} / 2}{\tan(55^\circ / 2)}$$

Then, calculating the actual distance using the ratio of real-world dimensions to perceived pixels:
$$Real Distance = \frac{17.0 \text{ cm} \times Focal Length}{Perceived Width_{px}}$$

## 🚧 Challenges Faced
1. **Ubuntu Installation For Dual-Booting**: While installing Ubuntu and allocating space for it, Even though I had 300GB free space and tried to allocate 100GB to Ubuntu, Windows was unable to shrink its volume because of bitlocker security files which were placed in between the free space obstructing and showing onoly a small amount of space available for shrinking. However I researched and learned that using a 3rd party partition manager would easily solve this issue and so I removed Bitlocker Security and then used a 3rd party tool in order create the unallocated space required for Ubuntu in order to dual-boot both Windows and Ubuntu.

2. **Math Module Input**: While using the math module, I forgot that the trignometric functions in the math module take radians as the input and not degrees which caused the wrong output, however I solved the issue but converting it beforehand.

3. **Logic Finding**: For finding the minimum wear cost in task 5 of medium dose, I was unable to think of the logic for calculating the possibility for every number for 3 different variables which satisfied the given criteria. Then I realised that this could be easily bypassed by giving the value of one of the variables as a function of the others which automatically takes care of the criteria and few if statements take care of the others as well.

4. **Shortest-Path Finding**: Though I figured out a method to use the shortest path to reach the destination using the breadth-first search method, I was unable to think of a way to display the path which it took. After some research I learned how to manipulate the queue in such a way that the shortest path was automatically calculated while the shortest path was used. I also forgot how when we store grid as a matrix the bottom most row of the grid will be the first element so it will be in inverted order and it took me a while to realize that and fix the code.

5. **Pin-Hole Camera and CV**: I had very little knowledge about these and was very hard for me to understand. However I spent some time to learn what and how Pin-Hole Cameras work and detected some basic errors which I was able to fix even though I was unable to learn to the full extend and see if the entire code was error free.
---

## 📚 Resources Used
* **Ubuntu Installation:**
    * https://youtu.be/mXyN1aJYefc?si=MjkGhq95SP9-VUqu

* **Numpy, Collections, Statistics Modules:**
    * https://www.geeksforgeeks.org/python/queue-in-python/
    * https://www.geeksforgeeks.org/python/queue-in-python/
    * https://www.geeksforgeeks.org/data-science/statistics-cheatsheet/

* **Linux Commands, Markdown, and Bash Scripting:** 
    * https://www.geeksforgeeks.org/linux-unix/linux-commands-cheat-sheet/
    * https://www.youtube.com/watch?v=bTVIMt3XllM
    * https://devhints.io/bash#conditionals

* **Behavior Tree Tutorial:** 
    * https://youtu.be/KeShMInMjro?si=Fk_HFlgc4v6OEeDV

* **Git and Github:**
    * https://www.youtube.com/watch?v=RGOj5yH7evk
