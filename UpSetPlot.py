import tkinter

import matplotlib

matplotlib.use('Agg')  # Disable GUI backend for headless use

import pandas as pd
import matplotlib.pyplot as plt
from upsetplot import UpSet, from_memberships
from tkinter import Tk, filedialog
import tkinter.messagebox as messagebox
import os
import warnings

# Optional: Silence future warnings from pandas/upsetplot
warnings.simplefilter(action='ignore', category=FutureWarning)


def main():

    description = ("Welcome to USPJJ, a tool for drawing UpSetPlots from provided data sets. Simply choose your Excel file and your plot will be prepared in no time.\n\n"
                   "Please make sure your Excel file follows this structure:\n"
    "• The first row must contain column headers.\n"
    "• One column should contain client names or IDs (can be ignored).\n"
    "• All other columns should contain 0 or 1 values.\n"
    "• The plot will show combinations of columns where value = 0.\n\n"
    "After clicking OK, you’ll be asked to select your Excel file.")
    messagebox.showinfo(title="USPJJ instructions", message=description)

    # Let user choose Excel file
    Tk().withdraw()  # Hide the root Tk window
    file_path = filedialog.askopenfilename(
        title="Select the Excel file",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )

    if not file_path:
        print("No file selected. Exiting.")
        messagebox.showinfo(title=None, message="No file selected. Exiting.")
        return

    messagebox.askquestion(title="", message="")

    try:
        # Load Excel file
        ef = pd.read_excel(file_path)

        # Drop 'CLIENT' column if it exists
        ef = ef.drop(columns=['CLIENT'], errors="ignore")

        # Generate memberships (columns with 0s)
        memberships = ef.apply(lambda row: tuple(col for col in ef.columns if row[col] == 0), axis=1)
        membership_counts = memberships.value_counts()
        upset_data = from_memberships(membership_counts.index.tolist(), data=membership_counts.values)

        # Create and save the plot
        fig = plt.figure(figsize=(12, 8))
        upset = UpSet(upset_data, show_counts='%d', sort_by='cardinality')
        upset.plot(fig=fig)
        fig.suptitle('Client Combinations with 0 in Parameters')

        # Save to same folder as input file
        output_path = os.path.join(os.path.dirname(file_path), "client_upset_plot.png")
        fig.savefig(output_path, dpi=300, bbox_inches="tight")
        plt.close(fig)

        print(f"\nPlot saved successfully at:\n{output_path}")

    except Exception as e:
        print(f"\nError: {str(e)}")


if __name__ == "__main__":
    main()
