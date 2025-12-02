def test_of_notebook():
    import matplotlib as matpl
    matpl.use("Agg")  # So the test does not open a window for the plt.show(), which has to be closed -> pytest hangs
    import src.step_3.notebook # noqa: E402