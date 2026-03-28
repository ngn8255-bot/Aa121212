This is a tiny Python project I made to learn about graphs and how to find the shortest path between points. It’s super simple—no fancy stuff, just basic code that works.
 
First, I built a  Graph  class to act like a little map. I can add points (called vertices) and draw one-way lines (edges) between them, with a number for how “long” or “costly” that line is. For example, if I want point A to connect to point B with a cost of 4, I just call  add_edge("A", "B", 4) .
 
Then, I used Dijkstra’s algorithm to find the shortest path from a starting point to all other points. It works like this: start at the first point, keep track of the shortest way to get to every other point, and always pick the next closest point to check next. It’s like planning the fastest route on a road trip map!
 
When I run the code, it prints out the shortest distance from my starting point to every other point. For example, from point A, the shortest way to E is 6—going A → C → D → E, instead of taking longer roads.
 
It’s not perfect, but it’s a fun way to see how graphs and shortest path algorithms work in real code. I learned a lot about how to structure data and how greedy algorithms pick the best next step.
 
 







