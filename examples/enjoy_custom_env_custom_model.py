import sys

from algorithms.appo.enjoy_appo import enjoy
from examples.train_custom_env_custom_model import register_custom_components, custom_parse_args


def main():
    """Script entry point."""
    register_custom_components()
    cfg = custom_parse_args(evaluation=True)
    status = enjoy(cfg)
    return status


if __name__ == '__main__':
    sys.exit(main())
