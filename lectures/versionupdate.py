def versiontuple(v):
    return tuple(map(int, (v.split("."))))

def need_install(module_name, version):
    install = False
    try:
        import importlib
        module = importlib.import_module(module_name)

        if versiontuple(module.__version__) < versiontuple(version):
            install = True
    except ModuleNotFoundError:
        install = True
    
    return install