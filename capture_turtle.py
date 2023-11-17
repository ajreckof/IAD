import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk, ImageGrab
import imageio
import numpy as np

class RecorderApp:
    def __init__(self, canvas, output_filename='recorded.gif'):
        self.canvas = canvas
        self.output_filename = output_filename
        self.is_recording = False
        self.frames = []

    def start_recording(self):
        self.is_recording = True
        self.record_window()

    def stop_recording(self):
        self.is_recording = False
        self.save_gif()

    def record_window(self):
        if self.is_recording:
            screenshot = self.capture_tkinter_window()
            if screenshot :
                self.frames.append(self.convert_frame_to_np(screenshot))
            self.canvas.after(100, self.record_window)  # Repeat after 100 milliseconds

    def capture_tkinter_window(self):
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        if w > 1 and h > 1 :
            x = self.canvas.winfo_rootx()
            y = self.canvas.winfo_rooty()
            screenshot = ImageGrab.grab(bbox=(x, y, x + w, y + h))
            return screenshot

    def convert_frame_to_np(self, frame):
        return np.array(frame)

    def save_gif(self):
        for frame in self.frames:
            print(shape_array(frame))
        if self.frames:
            imageio.mimsave(self.output_filename, self.frames, fps=10, loop = 0)

def shape_array(arr):
    try : 
        return (len(arr), *shape_array(arr[0]))
    except TypeError:
        return ()

if __name__ == "__main__":
    root = tk.Tk()
    canvas = Canvas(root, width=640, height=480, bg="white")
    canvas.pack()

    app = RecorderApp(canvas)
    
    # Manually start and stop recording
    app.start_recording()
    root.after(5000, app.stop_recording)  # Stop recording after 5000 milliseconds (adjust as needed)

    root.mainloop()
