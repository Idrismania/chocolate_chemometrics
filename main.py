import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path


def raw_to_spectrum_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extracts spectroscopy-related columns from the raw dataframe.

    Args:
        df: Original csv data loaded with pandas.

    Returns:
        dataframe with the relevant spectroscopy indeces extracted.
    """
    n_cols = df.shape[1]
    spectroscopy_indices = [i for i in range(n_cols) if i != 0 and i != n_cols - 2 and i != n_cols - 1]

    spectrum_data = df.iloc[:, spectroscopy_indices]

    return spectrum_data


def plot_mean_std_distribution(df: pd.DataFrame) -> None:
    """
    Plots the mean intensity and standard deviation of all sample spectra,
    given a data frame of wavelength intensities

    Args:
        df: Raw spectrum dataframe obtained from raw_to_spectrum_data().
    """

    # Calculate mean std
    mean_spectrum = df.mean()
    std_spectrum = df.std()

    fig, ax = plt.subplots()

    # Plotting
    ax.plot(df.columns, mean_spectrum, color="black", linewidth=1, label="Spectrum Mean")
    ax.fill_between(df.columns, mean_spectrum - std_spectrum, mean_spectrum + std_spectrum, color='black', alpha=0.2, edgecolor=None, label="Spectrum Standard Deviation")

    # Annotating
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("Intensity")
    ax.legend(loc="upper left")

    plt.show()



def main() -> None:

    df = pd.read_csv(Path("data", "df.csv"))

    spectrum_df = raw_to_spectrum_data(df)
    spectrum_df.columns = pd.to_numeric(spectrum_df.columns)

    plot_mean_std_distribution(spectrum_df)

    
    

if __name__ == "__main__":
    main()