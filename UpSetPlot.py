import platform
import subprocess
import matplotlib
import CustomMessage
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
from upsetplot import UpSet, from_memberships
from tkinter import Tk, filedialog
import tkinter.messagebox as messagebox
import os
import warnings

# Silence future warnings from pandas/upsetplot
warnings.simplefilter(action='ignore', category=FutureWarning)


def main():

    description = ("Welcome to USPJJ – a tool for visualizing data patterns using UpSet plots.\n"
    "To get started, simply select your Excel file. The plot will be generated automatically.\n\n"
    "Please ensure your Excel file follows this structure:\n"
    "• The first row must contain column headers.\n"
    "• The first column (e.g. names or IDs) will be dropped automatically. Make sure it doesn't contain values.\n"
    "• All other columns should contain only 0 or 1 values.\n\n"
    "Make sure the Excel file is closed before proceeding.\n\n"
    "The plot will show combinations of columns that match the selected value (0 or 1).\n\n"
    "After clicking OK, you’ll be prompted to choose your Excel file.")
    messagebox.showinfo(title="USPJJ instructions", message=description)

    # Let user choose Excel file
    file_path = filedialog.askopenfilename(
        title="Select the Excel file",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )

    print("[1] File selected:", file_path)

    if not file_path:
        print("No file selected. Exiting.")
        messagebox.showwarning(title="Script stopped!", message="No file selected. Terminating process.")
        return

    criteria_message = ("Choose whether you want to see groups that meet the criteria (value = 1) or that do not (value = 0).\n"
    "This doesn't affect the groups, only which value is used to define the combinations.")
    criteria = CustomMessage.ask_user_choice(criteria_message,
                                  "Match criteria", "Don't match criteria")

    print("[2] User criteria selected:", criteria)

    try:
        # Load Excel file
        ef = pd.read_excel(file_path)
        print("[3] File loaded:", ef.shape)

        # Drop the first column
        ef = ef.iloc[:, 1:]
        print("[4] First column dropped.")

        print("[5] Starting to generate memberships...")

        # Generate memberships
        memberships = ef.apply(lambda row: tuple(col for col in ef.columns if row[col] == criteria), axis=1)
        membership_counts = memberships.value_counts()
        upset_data = from_memberships(membership_counts.index.tolist(), data=membership_counts.values)
        print("[6] Memberships generated. Now counting...")

        # Create and save the plot
        fig = plt.figure(figsize=(12, 8))
        upset = UpSet(upset_data, show_counts='%d', sort_by='cardinality')
        upset.plot(fig=fig)

        if criteria == 1:
            plot_name = "UpSet plot - Matching criteria"
        else:
            plot_name = "UpSet plot - Non-matching criteria"

        fig.suptitle(plot_name)

        # Save to same folder as input file
        output_path = os.path.join(os.path.dirname(file_path), "UpSet_plot.png")
        fig.savefig(output_path, dpi=300, bbox_inches="tight")
        plt.close(fig)

        print(f"\nPlot saved successfully at:\n{output_path}")

        def open_file(path):
            if platform.system() == "Windows":
                os.startfile(path)
            elif platform.system() == "Darwin":  # macOS
                subprocess.call(["open", path])
            else:  # Linux
                subprocess.call(["xdg-open", path])

        open_file(output_path)
        messagebox.showinfo(title="Success!", message="UpSet plot successfully generated.")


    except Exception as e:
        print(f"\nError: {str(e)}")


if __name__ == "__main__":
    main()
