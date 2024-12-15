def __getattr__(name):
    if name in ['models', 'modules', 'pipelines', 'renderers', 'representations', 'utils']:
        import importlib
        return importlib.import_module(f".{name}", __name__)
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

__all__ = ['models', 'modules', 'pipelines', 'renderers', 'representations', 'utils']
