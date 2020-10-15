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
  

## Entrenamiento y validación 

Ejecutar en consola el siguiente comando.

python main.py --use_cuda --gpu 0 --batch_size 15 --n_epochs 50 --num_workers 1  --video_path ./data/image_data/  --dataset ucf101 --sample_size 240 --lr_rate 0.001 -- n_classes (numero de clases)



## Refeencias
* https://github.com/kenshohara/video-classification-3d-cnn-pytorch
* https://github.com/HHTseng/video-classification

 

