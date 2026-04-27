from pygame_widgets.button import Button

class NextButton():
    def __init__(self, win, onclickFunction, buttonText='Next Question'):
        self.button = Button(
            win,  # Surface to place button on
            140,  # X-coordinate of top left corner
            200,  # Y-coordinate of top left corner
            300,  # Width
            200,  # Height
            text=buttonText,  # Text to display
            fontSize=40,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=(50, 200, 100),  # Colour of button when not being interacted with
            hoverColour=(20, 170, 10),  # Colour of button when being hovered over
            pressedColour=(0, 200, 20),  # Colour of button when being clicked
            radius=20,  # Radius of border corners (leave empty for not curved)
            onClick=onclickFunction  # Function to call when clicked on
        )
