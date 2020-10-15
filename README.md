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


 2. 
  

## Preprocesamiento 
Once you have created the dataset, start training ->
 
python main.py --use_cuda --gpu 0 --batch_size 10 --n_epochs 80 --num_workers 0  --annotation_path ./data/annotation/ucf101_01.json --video_path ./data/image_data/ --sample_size 150 --lr_rate 0.01 --n_classes <num_classes>
```

## Note 
* All the weights will be saved to the snapshots folder 
* To resume Training from any checkpoint, Use
```
--resume_path <path-to-model> 
```


## Tensorboard Visualisation(Training for 4 labels from UCF-101 Dataset)
 


## Inference
 

## Refeencias
* https://github.com/kenshohara/video-classification-3d-cnn-pytorch
* https://github.com/HHTseng/video-classification

 

