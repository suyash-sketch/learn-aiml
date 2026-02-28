import subprocess
import sys


def check_nvidia_smi():
    print("=== Checking system GPU with nvidia-smi ===")
    try:
        result = subprocess.run(
            ["nvidia-smi"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if result.returncode == 0:
            print(result.stdout)
        else:
            print("nvidia-smi command failed or no NVIDIA GPU detected.")
            print(result.stderr.strip())
    except FileNotFoundError:
        print("nvidia-smi not found. NVIDIA drivers or CUDA toolkit may not be installed.")
    print()


def check_pytorch():
    print("=== Checking PyTorch CUDA support ===")
    try:
        import torch

        print(f"PyTorch version: {torch.__version__}")
        cuda_available = torch.cuda.is_available()
        print(f"torch.cuda.is_available(): {cuda_available}")
        if cuda_available:
            device_count = torch.cuda.device_count()
            print(f"Number of CUDA devices: {device_count}")
            for i in range(device_count):
                print(f"  Device {i}: {torch.cuda.get_device_name(i)}")
            print("Default device:", torch.device("cuda"))
        else:
            print("CUDA not available in PyTorch. Check your CUDA and PyTorch installation.")
    except ImportError:
        print("PyTorch (torch) is not installed in this Python environment.")
    print()


def check_tensorflow():
    print("=== Checking TensorFlow GPU support ===")
    try:
        import tensorflow as tf

        print(f"TensorFlow version: {tf.__version__}")
        gpus = tf.config.list_physical_devices("GPU")
        if gpus:
            print(f"GPUs detected by TensorFlow: {len(gpus)}")
            for gpu in gpus:
                print("  ", gpu)
        else:
            print("No GPUs detected by TensorFlow.")
    except ImportError:
        print("TensorFlow is not installed in this Python environment.")
    print()


def main():
    print("Python executable:", sys.executable)
    print("Python version:", sys.version)
    print()

    check_nvidia_smi()
    check_pytorch()
    check_tensorflow()


if __name__ == "__main__":
    main()

