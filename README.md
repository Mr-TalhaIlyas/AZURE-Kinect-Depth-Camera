# AZURE-Kinect-Depth-Camera

## [Official Repo](https://github.com/etiennedub/pyk4a/)
# pyk4a


![pyk4a](https://github.com/etiennedub/pyk4a/raw/master/figs/pyk4a_logo.png) 


This library is a simple and pythonic wrapper in Python 3 for the Azure-Kinect-Sensor-SDK.

Images are returned as numpy arrays and behave like python objects.

This approach incurs almost no overhead in terms of CPU, memory or other resources.
It also simplifies usage. Kinect C api image buffers are directly reused and image releases are performed automatically by the python garbage collector.

Homepage: https://github.com/etiennedub/pyk4a/

## Prerequisites
The [Azure-Kinect-Sensor-SDK](https://github.com/microsoft/Azure-Kinect-Sensor-SDK) is required to build this library.
To use the SDK, refer to the installation instructions [here](https://github.com/microsoft/Azure-Kinect-Sensor-SDK/blob/develop/docs/usage.md).


## Install

### Linux

Linux specific installation instructions [here](https://docs.microsoft.com/en-us/azure/kinect-dk/sensor-sdk-download#linux-installation-instructions)

Install both packages `libk4a<major>.<minor>` and `libk4a<major>.<minor>-dev`. The latter contains the headers and CMake files to build pyk4a.

Make sure your `LD_LIBRARY_PATH` contains the directory of k4a.lib

```shell
pip install pyk4a
```

### Windows

In most cases `pip install pyk4a` is enough to install this package.

When using an anaconda environment, you need to set the environment variable `CONDA_DLL_SEARCH_MODIFICATION_ENABLE=1` https://github.com/conda/conda/issues/10897

Because of the numerous issues received from Windows users, the installer ([setup.py](setup.py)) automatically detects the kinect SDK path.

When the installer is not able to find the path, the following snippet can help.
Make sure you replace the paths in these instructions with your own kinect SDK path. It is important to replace 1.4.1 with your installed version of the SDK.
```shell
pip install pyk4a --no-use-pep517 --global-option=build_ext --global-option="-IC:\Program Files\Azure Kinect SDK v1.4.1\sdk\include" --global-option="-LC:\Program Files\Azure Kinect SDK v1.4.1\sdk\windows-desktop\amd64\release\lib"
```

#### Commands
if you get error like `k4a.dll` not found on path
```
conda env config vars set CONDA_DLL_SEARCH_MODIFICATION_ENABLE=1
setx K4A_DLL_DIR "C:\Program Files\Azure Kinect SDK v1.4.1\sdk\windows-desktop\amd64\release\bin"
```
