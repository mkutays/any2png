from PyInstaller.utils.hooks import collect_all

datas, binaries, hiddenimports = list(), list(), list()

libs = [ "plotly", "kaleido"]
for lib in libs:
    datas_, binaries_, hiddenimports_ = collect_all(lib)
    datas += datas_
    binaries += binaries_
    hiddenimports += hiddenimports_


