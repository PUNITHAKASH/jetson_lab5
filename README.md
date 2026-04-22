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
<img width="1200" height="1600" alt="WhatsApp Image 2026-04-22 at 00 22 26 (1)" src="https://github.com/user-attachments/assets/9e9b3891-2b50-4ec7-8d65-fe6482866c08" />
<img width="1200" height="1600" alt="WhatsApp Image 2026-04-22 at 00 22 26" src="https://github.com/user-attachments/assets/64c40106-050c-4cad-bd85-d1ffe9ba6c23" />
<img width="1200" height="1600" alt="WhatsApp Image 2026-04-22 at 00 22 31" src="https://github.com/user-attachments/assets/0d34130d-8bf8-46cd-a545-6b1b3227b78a" />




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
