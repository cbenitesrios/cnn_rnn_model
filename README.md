# Seminario 2
Implementacion de un modelo de red CNN + RNN
 

#
## Prerequisitos
* PyTorch 
* FFmpeg
* Python 3
* Flask

## Preprocesamiento 
1. Ordenar los videos del dataset de la siguiente manera dentro de las carpeta ./data/video_data

  ```
   data 
       video_data    
              Abuso
              Disparo
              Normal 
                      normal1.mp4
                      normal2.mp4
                      normal3.mp4
  ```


 2. python ./utils/video_jpg.py
    python ./utils/n_frames.py
    python ./utils/gen_anns_list.py
    python ./utils/to_json.py 
  

## Preprocesamiento 


## Refeencias
* https://github.com/kenshohara/video-classification-3d-cnn-pytorch
* https://github.com/HHTseng/video-classification

 

