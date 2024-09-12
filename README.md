Button Descriptions:

    "Press Click":
        This button waits for the user to left or right-click anywhere on the screen. It captures the coordinates of the click and displays them in the interface. If a macro is being recorded, the click is stored as a step in the macro sequence.

    "Register Key":
        Allows the user to record a key press from the keyboard. The key pressed is displayed in the interface, and if a macro is being recorded, this event is also stored in the macro sequence.

    "Apply Delay":
        This button activates a field where you can input a delay time in seconds. The entered delay is applied, and if a macro is being recorded, the delay is stored as part of the sequence.

    "Apply Entered Delay":
        Applies the delay entered in the previous field and saves it in the macro if one is being recorded.

    "Record Macro":
        Starts or stops recording a macro. While recording, all clicks, keystrokes, and delays are saved in a sequence. Once stopped, the macro can be saved with a name into a JSON file to be replayed later.

    "Play":
        Allows you to play a previously saved macro. The user is prompted to enter the name of the macro they want to play, and the macro will be repeated as many times as the user specifies.

    "View Macros":
        Opens a window showing all saved macros. From this window, you can select a macro to play or delete it.

    "Search Text on Screen":
        Allows you to search for text on the screen using a spiral movement technique that takes screenshots. If the specified text is found, it automatically clicks on the screen. If a macro is being recorded, this action will also be saved in the sequence.
