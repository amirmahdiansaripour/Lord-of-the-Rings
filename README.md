# Lord of the Rings
Comparison of different search algorithms in artificial intelligence.

This project is an extension of the [second assignment of the Artificial Intelligence Course](https://github.com/amirmahdiansaripour/Artificial-Inteligence-Assigments) I have taken in the University of Tehran, Spring 2022. The project is about different searching mehtods (BFS, DFS, IDS, and Astar), and demonstrates how they differ in the way their frontier and explored sets are updated.

How to run :

Make sure that the pygame library is installed on your OS for graphical interface.

`
python3 total.py
`

A window will be shown, in which the pieces of the game should be placed (Gandalf, Orcs, and The Castle). You can switch between cells in the grid by clicking → ↑ ↓ ← 

![12](https://github.com/amirmahdiansaripour/test/assets/92050925/dd0b1488-5465-4f0e-a9d0-0e01bbdc5a2e)


After clicking 'f' to finish locating the pieces, the kind of algorithm is asked:

If you enter IDS, the maximum depth is asked as the second input. If you enter A*, the weight is asked. (No additional input is required for BFS and DFS).

![13](https://github.com/amirmahdiansaripour/test/assets/92050925/ea032f73-98d0-4976-9925-3dc6707f6d99)

The algorithm will then run and the Gandalf might reach the Castle (He should not hit the Orcs!) 

![14](https://github.com/amirmahdiansaripour/test/assets/92050925/3a18e4a9-34a2-4713-9c9c-49578bfb4038)

A simple BFS example (run on windows using Visual Studio Code and Anaconda):



https://github.com/amirmahdiansaripour/Lord-of-the-Rings/assets/92050925/0495c32d-d0f7-425f-a71f-2d3dbe667eba




Please see the report included in the repository for more details and a thorough explanation about the project and search algorithms (their time/memory complexity, heuristic methods, etc.)



