# Acoustic_Camera_3D_Measurement_EXP

# Project Introduction
This project presents a lightweight and efficient method for 3D seabed target measurement using a single forward-looking sonar (FLS), specifically the ARIS EXPLORER 3000 (Acoustic Camera). 
Designed for low-altitude operations, the approach exploits acoustic cast shadow information to infer the height of underwater targets from two sonar frames.

# Scene Illustration
This project leverages acoustic cast shadow information observed from two viewpoints to estimate the height and 3D shape of seafloor objects. By analyzing changes in shadow geometry across frames, we infer spatial structure in a fast and lightweight pipeline suitable for real-time deployment on autonomous underwater vehicles (AUVs) operating in low-visibility and confined environments.
![Scene Illustration](https://github.com/user-attachments/assets/9f3f9b57-ca01-46df-801b-2f26085c217b)
The acoustic camera provides two data formats: the original displaced polar-coordinate raw data and the converted Cartesian-coordinate images.
The latter supports both grayscale and pseudo-color display modes.

# Acoustic Cast Shadow Demo
An acoustic cast shadow is the dark region in a sonar image caused when an object on the seafloor blocks acoustic waves, preventing them from reaching the area behind it. 
The shadow's shape and length are closely related to the object's height and the sonar's viewing angle, making it a key cue for 3-D information inference from sonar imagery.
![Acoustic cast shadows demo](https://github.com/user-attachments/assets/d3c3d786-7a46-4db6-b6ee-8371fd49ab1e)


# Acoustic Data Processing
Metafile initialization: [https://github.com/SoundMetrics/aris-integration-sdk]
Acoustic simulation: [https://github.com/sollynoay/Sonar-simulator-blender]

An enhanced version featuring adaptive shadow modeling for varying seafloor geometries and sonar altitudes is currently under development.

# Acknowledgment
The authors would like to thank Sound Metrics Corp.[https://github.com/SoundMetrics/aris-integration-sdk] for their valuable technical insights and knowledge sharing in the areas of underwater acoustic data acquisition and lightweight processing, which greatly supported the development of this project.
