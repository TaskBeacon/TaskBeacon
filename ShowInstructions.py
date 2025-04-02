import os
from psychopy import visual, event
from TaskFunc import img_path  # Assuming img_path is defined in __init__.py

def ShowInstructions(win, use_image=True, text=None, image_file='MID_Instructions0.bmp', continue_key='space'):
    """
    Displays instructions either as text or an image.

    Args:
        win (visual.Window): The PsychoPy window object.
        use_image (bool, optional): If True, display an image. If False, display text. Defaults to True.
        text (str, optional): The instruction text to display (only used if use_image is False). Defaults to None.
        image_file (str, optional): The name of the image file to load (only used if use_image is True).
                                     Assumes the image is in the 'img' folder. Defaults to 'MID_Instructions0.bmp'.
        continue_key (str, optional): The key that the user needs to press to continue. Defaults to 'space'.
    """
    if use_image:
        instruction_image_path = os.path.join(img_path, image_file)
        try:
            ins = visual.ImageStim(win, image=instruction_image_path, pos=[0, 0])
        except FileNotFoundError:
            print(f"Error: Instruction image not found at {instruction_image_path}")
            core.quit()
    else:
        if text is None:
            print("Error: No instruction text provided when use_image is False.")
            core.quit()
        ins = visual.TextStim(win, text=text, height=.6, wrapWidth=25, color='black', pos=[0, 0])

    while not event.getKeys(keyList=[continue_key]):
        ins.draw()
        win.flip()