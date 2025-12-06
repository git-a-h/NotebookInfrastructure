def test_of_notebook():
    import matplotlib as plt

    plt.use(
        "Agg"
    )  # So the test does not open a window for the plt.show(), which has to be closed -> pytest hangs
    import src.step_3.notebook  # noqa: F401

    # F401 is imported but unused, but is run during smoketest (see htmlcoverage)
