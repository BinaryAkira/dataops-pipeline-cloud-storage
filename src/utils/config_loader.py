from pathlib import Path
import tomllib


def load_config(path: str = "config/config.toml") -> dict:
    """Load a TOML configuration file.

    Parameters
    ----------
    path : str
        Path to the TOML config file.

    Returns
    -------
    dict
        Parsed configuration dictionary.

    Raises
    ------
    FileNotFoundError
        If the config file does not exist.
    """
    config_path = Path(path)

    if not config_path.exists():
        msg = f"Config file not found at: {config_path}"
        raise FileNotFoundError(msg)

    with config_path.open("rb") as file:
        return tomllib.load(file)
