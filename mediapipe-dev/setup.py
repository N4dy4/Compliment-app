import os
import re
import subprocess
from setuptools import setup, find_packages

# Load the package's version
def get_version():
    version = "0.1.0"  # replace with your actual version if different
    if not re.match(r"^\d+\.\d+\.\d+$", version):
        raise ValueError("Invalid version format. Please use MAJOR.MINOR.PATCH format (e.g., 0.1.0).")
    return version

# Parse requirements from requirements.txt
def parse_requirements():
    requirements_file = "requirements.txt"
    if not os.path.isfile(requirements_file):
        raise FileNotFoundError(f"{requirements_file} not found in the project root.")
    with open(requirements_file, "r") as f:
        return f.read().splitlines()

# Check if Bazel is installed and the version is sufficient
def check_bazel():
    try:
        output = subprocess.check_output(["bazel", "--version"], text=True)
        version = output.split()[1]
        major, minor, patch = map(int, version.split("."))
        min_version = (3, 4, 0)
        if (major, minor, patch) < min_version:
            raise ValueError(f"Bazel version {version} is too low. Minimum required version is 3.4.0.")
    except FileNotFoundError:
        raise RuntimeError("Bazel is not installed. Please install Bazel to proceed.")

# Check if protoc is installed and accessible
def check_protoc():
    try:
        subprocess.check_output(["protoc", "--version"])
    except FileNotFoundError:
        raise RuntimeError("protoc (Protocol Buffers Compiler) is not installed. "
                           "Install with 'apt install protobuf-compiler' on Linux or 'brew install protobuf' on macOS.")

# Check Python version compatibility
def check_python_version():
    min_version = (3, 6)
    if os.sys.version_info < min_version:
        raise RuntimeError(f"Python {min_version[0]}.{min_version[1]}+ is required.")

# Run setup checks
def setup_checks():
    check_bazel()
    check_protoc()
    check_python_version()

# Call setup checks
setup_checks()

# Package setup
setup(
    name="my_mediapipe_project",
    version=get_version(),
    description="A MediaPipe-based Python project",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=parse_requirements(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
