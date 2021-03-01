# SSD-Mobilenet

This is use MobileNetv1, MobileNetv2 and MobileNetv3 implement Single Shot Detector(SSD).  


## Requriments
I use tensorflow2 implenment.
```
pip install -r requirments.txt
```

## Train
Step 1: Modify `config.py`  
```
    EPOCHS : The number of iteration. 
    BATCH_SIZE: You can modify size, according to your GPU.

    CLASSES: You want to train classes.
    
    DATASET : Dataset path
    VOC_TEXT_FILE: Dataset train, val, test images information.
    VOC_TRAIN_FILE: Produce train text file.

    MODEL_FOLDER : Stroage weigth folder
    FILE_NAME : Storage weigth weight
```
Step 2: `pip install voc_annotation.py`
You can obtain three text files(train.txt, val.txt and test.txt)  
  
Step 3: `pip install train_300.py`  

## Test
You can look `predict_image.ipynb`.  

### Execute results
![image01](./image/06694_result.jpg)

## Evalutate model
Step 1: You need use `pip install predict_text.py` produce predicted results' text file.  
Step 2: `pip install evaluate.py`  


## Reference
[Mobilenet-SSD-Essay](https://github.com/bubbliiiing/Mobilenet-SSD-Essay)  
[MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/abs/1704.04861)  
[MobileNetV2: Inverted Residuals and Linear Bottlenecks](https://arxiv.org/abs/1801.04381)  
[Searching for MobileNetV3](https://arxiv.org/abs/1905.02244)  
