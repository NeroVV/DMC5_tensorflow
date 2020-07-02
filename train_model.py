import numpy as np
from Alexnet import alexnet2

WIDTH = 70
HEIGHT = 40
LR = 1e-3
EPOCHS = 10

MODEL_NAME = 'model_DMC5/DMC5-{}-{}-epochs.model'.format(LR, 'alexnetv2')

file_name = 'training_data_balance.npy'

model = alexnet2(WIDTH,HEIGHT,LR)

train_data = np.load(file_name,allow_pickle=True)

print(len(train_data))

train = train_data[:-23000]
test = train_data[-23000:]

X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
Y = [i[1] for i in train]

test_X = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
test_Y = [i[1] for i in test]

model.fit({'input': X}, {'targets': Y}, n_epoch = EPOCHS,
          validation_set = ({'input': test_X}, {'targets': test_Y}),
          snapshot_step = 1380, show_metric=True, run_id = MODEL_NAME)

# tensorboard --logdir=foo:C:/DMC_tensorflow/log

# cd C:\DMC_tensorflow\log\model_DMC5\DMC5-0.001-alexnetv2-epochs.model
# tensorboard --logdir ./ --host=127.0.0.1

model.save(MODEL_NAME)
