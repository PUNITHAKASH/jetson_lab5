# Lab 5: Stark Industries Anomaly Detector
**Author:** Punith Akash Balachandran  
**Institution:** University of Maryland, Baltimore County (UMBC)  
**Course:** DATA 690 - Real-Time AI & Edge Computing  

##  Project Overview
This project implements a real-time object detection system on an NVIDIA Jetson platform using the **SSD-Mobilenet-v2** architecture. I developed a custom **Iron Man-themed HUD (Heads-Up Display)** that provides a visual security interface. The system is designed to monitor environment status and trigger a high-priority "Anomaly Alert" when specific restricted objects are detected.

##  Technical Implementation
* **Inference Engine:** Utilizes NVIDIA's `jetson-inference` library and TensorRT for hardware-accelerated deep learning.
* **Modular Codebase:** Separated the core detection logic (`main_detector.py`) from the UI rendering engine (`ui_stark.py`) for optimized performance and maintainability.
* **Custom HUD Logic:**
    * **Scanning Mode (Blue):** System is active and tracking nominal objects.
    * **Anomaly Mode (Red):** Triggered upon detection of "Cell Phones" or "Bottles" (Class IDs 77 and 44).

##  Challenges & Solutions
During the deployment phase, several environment-specific issues were resolved:
* **Manual Compilation:** Successfully configured and compiled the `jetson-inference` Python 3.8 bindings from source.
* **Linker Resolution:** Patched a critical build failure related to `libnpymath.a` by manually mapping the NumPy library paths in the C++ linker settings.
* **Portable Deployment:** Included compiled `.so` (Shared Object) binaries within the project directory to ensure environment portability across different JetPack configurations.

##  Detection Evidence
The following screenshot demonstrates the system accurately identifying a restricted object and transitioning the HUD to the **Red "!!! ANOMALY !!!"** state.

![Anomaly Detection Screenshot](screenshot.jpg)

## 📁 Repository Structure
* `main_detector.py`: Primary application entry point.
* `ui_stark.py`: Custom OpenCV-based HUD rendering module.
* `jetson_inference_python.so`: Compiled inference engine for Python 3.8.
* `jetson_utils_python.so`: Compiled utility/camera engine for Python 3.8.
* `jetson/`: Python library wrappers.

## ⚙️ How to Run
Ensure you are in the project root directory and execute:
```bash
python3 main_detector.py
