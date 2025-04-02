from psychopy import visual, event, core
import os

def ShowInstructions(win, use_image=True, img_file='img/instructions.bmp', intro_text=None, continue_key='space'):
    """
    Display task instructions in either text or image format.

    Args:
        win (visual.Window): The PsychoPy window object.
        use_image (bool): If True, display an image; if False, show text. Default is True.
        img_file (str): Path to the image file to display (used only if use_image=True).
        intro_text (str): Text content to show (used only if use_image=False).
        continue_key (str): Key that participant must press to continue. Default is 'space'.
    """
    
    # Switch to text if intro_text is provided
    if intro_text is not None:
        use_image = False

    if use_image:
        if not os.path.exists(img_file):
            print(f"[Error] Image file not found: {img_file}")
            core.quit()
        instruction_stim = visual.ImageStim(win, image=img_file, pos=(0, 0))
    else:
        if not isinstance(intro_text, str) or not intro_text.strip():
            print("[Error] Invalid or missing instruction text.")
            core.quit()
        instruction_stim = visual.TextStim(win, text=intro_text, height=0.6, wrapWidth=25, color='black', pos=(0, 0))

    while not event.getKeys(keyList=[continue_key]):
        instruction_stim.draw()
        win.flip()
