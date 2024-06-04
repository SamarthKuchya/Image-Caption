import numpy as np
import pickle
from keras.applications.resnet import ResNet50, preprocess_input
from keras.preprocessing import image
from keras.models import Model, load_model
from keras.utils import pad_sequences
import keras.utils as image

model=load_model('model29.h5')

model_temp=ResNet50(weights='imagenet',input_shape=(224,224,3))

model_resnet=Model(model_temp.input,model_temp.layers[-2].output)

def preprocess_img(img):
    img=image.load_img(img,target_size=(224,224))
    img=image.img_to_array(img)
    img=np.expand_dims(img,axis=0)
    
#     Normlisation
    img=preprocess_input(img)
    return img

def encode_image(img):
    img=preprocess_img(img)
    print(img.shape)
    feature_vector=model_resnet.predict(img)
    feature_vector=feature_vector.reshape((1,feature_vector.shape[1]))
    print(feature_vector.shape)
    return feature_vector

# enc=encode_image('./image.jpeg')

with open('word_to_idx.pkl','rb') as f:
    word_to_idx=pickle.load(f)
    
with open('idx_to_word.pkl','rb') as f:
    idx_to_word=pickle.load(f)

def predict_caption(photo):
    photo=encode_image(photo)
    in_text='startseq'
    max_len=35
    for i in range(max_len):
        sequence=[word_to_idx[w] for w in in_text.split() if w in word_to_idx]
        sequence=pad_sequences([sequence],maxlen=max_len,padding='post')
        
        ypred=model.predict([photo,sequence])
        ypred=ypred.argmax() #words with max probability always - Greedy Sampling
        word=idx_to_word[ypred]
        in_text+=(' '+word)
        
        if word=='endseq':
            break
        
    final_caption=in_text.split()[1:-1]
    final_caption=' '.join(final_caption)
    
    return final_caption

print('done')

# print(predict_caption('./image.jpeg'))
