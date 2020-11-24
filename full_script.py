from tensorflow.keras.layers import Dense
from sklearn.datasets import make_classification
from tensorflow.keras.callbacks import Callback
from tensorflow.keras.models import Sequential
from tensorflow.keras import backend as K
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold, train_test_split

#Make sure twilio is installed 
#use pip install twilio
from twilio.rest import Client

#Creating the function to send text message¶
def send_message(text):
    account_sid = 'account_ID' #Can be obtained from Twilio Console
    auth_token = 'auth_token'  #Can be obtained from Twilio Console
    client = Client(account_sid, auth_token)

    message = client.messages \
    .create(
         from_='whatsapp:+14155238886',
         body=text,
         to='whatsapp:+918*********'
     )

#Creating a custom callback
class WhatsappCallBack(Callback): 
    '''
    Creating a custom callback in keras. For more info, see https://www.tensorflow.org/guide/keras/custom_callback and 
    https://keunwoochoi.wordpress.com/2016/07/16/keras-callbacks/
    '''
    def on_train_begin(self, logs = None):
        self.losses = [] #Initializing the list of losses
        send_message("The training has started") #Sending message on whatsapp at the beginning of the training

    def on_epoch_begin(self, epoch, logs = None):
        pass


    def on_epoch_end(self, epoch, logs = None):
        self.losses.append(logs['loss'])

    def on_train_end(self, logs = None):
        send_message("The training has ended") #Sending message on whatsapp at the end of the training
        send_message(self.losses)

#Function to return a very simple ANN
def create_model():
    model = Sequential()
    model.add(Dense(60, input_dim=20, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    return model

cb = WhatsappCallBack() #Creating an instance of our custom Callback

#Creating a sample dataset and testing our model¶
x,y = make_classification(n_samples=1000, n_classes=2, n_features=20)
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.3)

model = create_model() #Creating an instance of our model

model.fit(x_train,y_train,batch_size=32, epochs=20, callbacks=[cb2], verbose=1) #Fitting the model
