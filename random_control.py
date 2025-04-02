import numpy as np
import random

def setup_seed(mode="indiv", subject_id=None, total_blocks=1, custom_seed=None, verbose=True):
    """
    Return general and block-level seeds for reproducible randomization.

    Args:
        mode (str): 'random', 'same', or 'indiv'.
        subject_id (str/int, optional): Required for 'indiv' mode.
        total_blocks (int): Number of blocks for which to generate seeds.
        custom_seed (int, optional): Override seed value.
        verbose (bool): Print summary if True.

    Returns:
        general_seed (int or None): Seed used for global or block generation.
        block_seeds (np.ndarray or None): Array of int seeds per block.
    """
    if mode == "random":
        if verbose:
            print("[INFO] Randomization mode: fully random (no seed).")
        return None, None

    # Resolve seed
    if custom_seed is not None:
        general_seed = int(custom_seed)
        label = f"custom={general_seed}"
    elif mode == "same":
        general_seed = 123
        label = "shared=123"
    elif mode == "indiv":
        try:
            general_seed = int(subject_id)
            label = f"subject ID={subject_id}"
        except (TypeError, ValueError):
            raise ValueError("In 'indiv' mode, provide a valid numeric subject_id.")
    else:
        raise ValueError(f"Invalid mode '{mode}'. Use 'random', 'same', or 'indiv'.")

    # Create block seeds (without changing global RNG)
    rng = np.random.default_rng(general_seed)
    block_seeds = rng.integers(0, 1e6, size=total_blocks)

    if verbose:
        print(f"[INFO] Randomization mode: {mode} ({label})")
        print(f"[INFO] General seed: {general_seed}")
        print(f"[INFO] Per-block seeds: {block_seeds}")

    return general_seed, block_seeds

def setup_seed_for_settings(settings, subdata, mode="indiv", custom_seed=None, verbose=True):
    """
    Wrapper to configure seed values and inject them into settings.

    Args:
        settings (SimpleNamespace): Settings object to update.
        subdata (list): Subject info; subdata[0] should be subject ID.
        mode (str): One of 'random', 'same', or 'indiv'.
        custom_seed (int, optional): Manually override general seed.
        verbose (bool): Whether to print logs.

    Returns:
        settings (SimpleNamespace): Updated with GeneralSeed and blockSeed.
    """
    subject_id = subdata[0] if len(subdata) > 0 else None
    total_blocks = getattr(settings, "TotalBlocks", 1)

    general_seed, block_seeds = setup_seed(
        mode=mode,
        subject_id=subject_id,
        total_blocks=total_blocks,
        custom_seed=custom_seed,
        verbose=verbose
    )

    settings.GeneralSeed = general_seed
    settings.blockSeed = block_seeds
    return settings