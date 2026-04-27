from pygame_widgets.button import Button

class NextButton():
    def __init__(self, win, onclickFunction, buttonText='Next Question'):
        self.button = Button(
            win,  # Surface to place button on
            160,  # X-coordinate of top left corner
            200,  # Y-coordinate of top left corner
            300,  # Width
            150,  # Height
            text=buttonText,  # Text to display
            fontSize=48,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
            hoverColour=(150, 0, 0),  # Colour of button when being hovered over
            pressedColour=(0, 200, 20),  # Colour of button when being clicked
            radius=20,  # Radius of border corners (leave empty for not curved)
            onClick=onclickFunction  # Function to call when clicked on
        )
