This project is a visualizer for insertion sort, bubble sort, quick sort, and merge sort.
STARTING IT:
Just run the main file
Once the main file is run, click on the buttons of the sorting algorithms you want visualized.  Bubble sort is automatically selected. 
Click again to de-select buttons.  You can also change the number of values in the random list to be sorted.  
Once all your choices have been input, click on start.  It won't start with no algorithms selected.

NOTES ON VISUALIZATION:
Not all algorithms are 100% accurate representations of their sorting functions.  (Namely merge and quick sort)
For example, even though merge sort is a recursive function, it goes through every subset of the list.
This is despite the fact it should be dividing the list in half and recursively sorting.
The reason for this is I intend this mostly to explain sorting algorithms to people unfamiliar with them, and I find the incorrect visualization easier to explain.
I plan to add support for accurate sorting algorithm visualization in the future.

ABOUT THE CODE:
For each sorting algorithm, the first function in their file is a normal implementation of the sorting algorithm, not used in the visualizer.
There is also a Sorter class for that algorithm that stores the list and has a function that allows the sorter to advance to the next step.
This is the only way to sort the sorter class, step by step, so it must be looped over.  If called once the list is sorted, nothing should happen.
There are also pygame UI elements, something I designed for this project with the intension of using them more in future projects.
The Text class allows you to easily display and modify customizable text in pygame.
The Button class allows you to create interactable and customizable buttons that can run functions.
The Input class allows you to create customizable inputs that you can get the values from.
There is also a simple random list generator included as well as a result verifier, which can be used to confirm a list was correctly sorted.

FUTURE PLANS:
- As previously mentioned, adding accurate sorting algorithm visualization in the future.
- Expanding the number of sorting algorithms usable
- Step by step visualization
